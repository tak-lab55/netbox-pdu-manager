# NetBox PDU Manager

Raritan PDU management plugin for NetBox 4.5+

## Overview

NetBox PDU Manager is a NetBox plugin for managing Raritan Power Distribution Units (PDUs) and their outlets. It provides comprehensive tracking of PDU devices, outlet configurations, connected devices, and power specifications.

## Features

### v0.1.0 (Current)

- **PDU Management**: Full CRUD operations for PDU devices
  - Basic information (name, manufacturer, model, serial number)
  - Network configuration (IP address, API URL, credentials)
  - Physical location (site, rack, rack position)
  - Power specifications (voltage, current, outlet count, phase)
  - Raritan-specific attributes (PDU type, firmware version)

- **Outlet Management**: Complete outlet (port) tracking
  - Outlet number and custom naming
  - Status tracking (on/off/unknown/error)
  - Connected device relationships
  - Phase and bank number for multi-phase PDUs
  - Power measurement fields (for future API integration)

- **User Interface**
  - Intuitive list and detail views
  - Outlet statistics dashboard on PDU detail page
  - Searchable and filterable lists
  - NetBox standard features (custom fields, tags, comments)

### Phase 2 (Planned)

- Raritan API integration for real-time monitoring
- Background tasks (Celery) for periodic data collection
- Power consumption graphs and dashboards
- Remote outlet control (on/off operations)
- Historical power measurement tracking

## Compatibility

- **NetBox**: 4.5.0 - 4.9.99
- **Python**: 3.10, 3.11, 3.12
- **Target PDU**: Raritan PX2, PX3, PX4 series

## Installation

### Step 1: Install the plugin

```bash
cd /opt/netbox
source venv/bin/activate
pip install netbox-pdu-manager
```

Or for development installation:

```bash
git clone https://github.com/yourusername/netbox-pdu-manager.git
cd netbox-pdu-manager
pip install -e .
```

### Step 2: Enable the plugin

Add the plugin to your NetBox configuration file (`/opt/netbox/netbox/netbox/configuration.py`):

```python
PLUGINS = [
    'netbox_pdu_manager',
]

# Plugin configuration (optional)
PLUGINS_CONFIG = {
    'netbox_pdu_manager': {
        'enable_api_sync': False,  # Reserved for Phase 2
        'sync_interval': 300,      # Reserved for Phase 2
    }
}
```

### Step 3: Run database migrations

```bash
cd /opt/netbox/netbox
python manage.py migrate
```

### Step 4: Restart NetBox

```bash
sudo systemctl restart netbox netbox-rq
```

## Usage

### Adding a PDU

1. Navigate to **Plugins > PDUs** in the NetBox UI
2. Click **Add** button
3. Fill in the PDU information:
   - **Basic**: Name, manufacturer, model, serial number, PDU type
   - **Location**: Site, rack, rack position
   - **Network**: IP address, API URL (for future API integration)
   - **Power**: Rated voltage, current, outlet count, phase
4. Save the PDU

### Managing Outlets

1. From a PDU detail page, you can view all associated outlets
2. Add outlets via **Plugins > Outlets > Add**
3. Configure:
   - PDU relationship
   - Outlet number and name
   - Status (on/off/unknown)
   - Connected device (optional)
   - Phase and bank (for multi-phase PDUs)

### Filtering and Search

- Use the filter panel on list views to narrow results by:
  - Site, Rack
  - Manufacturer, Model
  - PDU Type
  - Status (for outlets)
- Quick search searches across name, manufacturer, model, and serial number

## Data Model

### PDU

A PDU represents a physical power distribution unit device.

**Key fields:**
- `name`: Unique identifier
- `manufacturer`: PDU manufacturer (default: Raritan)
- `model`: PDU model number
- `pdu_type`: Raritan PDU type (PX2/PX3/PX4)
- `site`: NetBox Site (required)
- `rack`: NetBox Rack (optional)
- `ip_address`: NetBox IPAddress (optional)
- `rated_voltage`: Voltage rating in volts
- `rated_current`: Current rating in amps
- `outlet_count`: Total number of outlets

### Outlet

An outlet represents an individual power port on a PDU.

**Key fields:**
- `pdu`: Parent PDU (required)
- `outlet_number`: Physical port number
- `name`: Custom name (optional)
- `status`: Power status (on/off/unknown/error)
- `connected_device`: NetBox Device (optional)
- `phase`: Electrical phase (for multi-phase PDUs)
- `last_measured_*`: Power measurement fields (for Phase 2)

## Development

### Project Structure

```
netbox-pdu-manager/
├── netbox_pdu_manager/
│   ├── __init__.py          # Plugin configuration
│   ├── models.py            # Data models (PDU, Outlet)
│   ├── views.py             # Views (list, detail, edit, delete)
│   ├── urls.py              # URL routing
│   ├── forms.py             # Forms for data entry
│   ├── tables.py            # Table definitions for list views
│   ├── filtersets.py        # Filter and search logic
│   ├── navigation.py        # Navigation menu items
│   ├── choices.py           # Choice sets (PDU types, statuses)
│   ├── templates/           # HTML templates
│   └── migrations/          # Database migrations
├── README.md
├── LICENSE
└── pyproject.toml
```

### Running Tests

```bash
# Coming soon
pytest
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/netbox-pdu-manager/issues)
- **Documentation**: [NetBox Plugin Development](https://netboxlabs.com/docs/netbox/plugins/development/)

## Roadmap

- [x] v0.1.0: Basic PDU and outlet management
- [ ] v0.2.0: Raritan API client integration
- [ ] v0.3.0: Background data synchronization (Celery)
- [ ] v0.4.0: Power monitoring and graphing
- [ ] v0.5.0: Remote outlet control

## Credits

Built with [NetBox](https://github.com/netbox-community/netbox) plugin framework.

## Changelog

### v0.1.0 (2026-02-09)

- Initial release
- PDU management (CRUD operations)
- Outlet management (CRUD operations)
- NetBox 4.5+ compatibility
- Basic UI with list and detail views
- Search and filtering capabilities
# netbox-pdu-manager
