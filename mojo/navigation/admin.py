from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django_mptt_admin.admin import DjangoMpttAdmin as MPTTModelAdmin

from .models import Item


class ItemAdmin(MPTTModelAdmin):
    """
    Admin class for the ItemAdmin class.
    """
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('href', )
    fieldsets = (
        (_('Basic settings'), {
            'fields': ('parent', 'name', 'slug', )
        }),
        ('URL', {
            'fields': ('url', ('content_type', 'object_id'), 'href'),
            'description': _("The URL for this navigation item, it can be "
                             "an absolute or relative URL, a django url pattern "
                             "or a generic relation to a model that supports get_absolute_url()"
                             "The url field has priority upon the generic relation."
                             "The link field displays the generated url.")
        }),
        (_('Access settings'), {
            'classes': ('collapse',),
            'fields': ('access_loggedin', 'access_group', 'access_permissions')
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': ('css_class', 'is_new_tab')
        })
    )
    level_limit = None

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Overrides parent class formfield_for_foreignkey method."""
        # If level_limit is set filter levels depending on the limit.
        if db_field.name == "parent" and self.level_limit is not None:
            kwargs["queryset"] = self.model.objects.filter(level__lt=self.level_limit)
        return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def do_move(self, instance, position, target_instance):
        """
        Overwritting parent do_move method to disallow users to exceed the self.level_limit value when drag and
        dropping items.
        """
        if position == 'inside' and self.level_limit >= 0 and target_instance.level >= self.level_limit:
            raise Exception(_(u'The maximum level for this model is %d' % self.level_limit))
        super(ItemAdmin, self).do_move(instance, position, target_instance)

admin.site.register(Item, ItemAdmin)
