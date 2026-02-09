from netbox.plugins import PluginConfig


class NetBoxPDUManagerConfig(PluginConfig):
    name = 'netbox_pdu_manager'
    verbose_name = 'NetBox PDU Manager'
    description = 'Raritan PDU management plugin for NetBox'
    version = '0.1.0'
    author = 'Your Name'
    author_email = 'your.email@example.com'
    base_url = 'pdu-manager'
    min_version = '4.5.0'
    max_version = '4.9.99'
    required_settings = []
    default_settings = {
        'enable_api_sync': False,  # Phase 2で使用
        'sync_interval': 300,      # Phase 2: 秒単位
    }


config = NetBoxPDUManagerConfig
