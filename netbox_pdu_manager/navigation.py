from netbox.plugins import PluginMenuButton, PluginMenuItem
from netbox.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_pdu_manager:pdu_list',
        link_text='PDUs',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_pdu_manager:pdu_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_pdu_manager:outlet_list',
        link_text='Outlets',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_pdu_manager:outlet_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        )
    ),
)
