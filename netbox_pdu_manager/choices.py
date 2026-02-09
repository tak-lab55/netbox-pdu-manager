from utilities.choices import ChoiceSet


class PDUTypeChoices(ChoiceSet):
    """Raritan PDU type choices"""
    key = 'PDU.pdu_type'

    TYPE_RARITAN_PX2 = 'raritan_px2'
    TYPE_RARITAN_PX3 = 'raritan_px3'
    TYPE_RARITAN_PX4 = 'raritan_px4'
    TYPE_GENERIC = 'generic'

    CHOICES = [
        (TYPE_RARITAN_PX2, 'Raritan PX2', 'blue'),
        (TYPE_RARITAN_PX3, 'Raritan PX3', 'blue'),
        (TYPE_RARITAN_PX4, 'Raritan PX4', 'blue'),
        (TYPE_GENERIC, 'Generic PDU', 'gray'),
    ]


class OutletStatusChoices(ChoiceSet):
    """Outlet power status choices"""
    key = 'Outlet.status'

    STATUS_ON = 'on'
    STATUS_OFF = 'off'
    STATUS_UNKNOWN = 'unknown'
    STATUS_ERROR = 'error'

    CHOICES = [
        (STATUS_ON, 'On', 'green'),
        (STATUS_OFF, 'Off', 'red'),
        (STATUS_UNKNOWN, 'Unknown', 'gray'),
        (STATUS_ERROR, 'Error', 'orange'),
    ]


class PhaseChoices(ChoiceSet):
    """Electrical phase choices for multi-phase PDUs"""
    key = 'Outlet.phase'

    PHASE_A = 'A'
    PHASE_B = 'B'
    PHASE_C = 'C'
    LINE_1 = 'L1'
    LINE_2 = 'L2'
    LINE_3 = 'L3'

    CHOICES = [
        (PHASE_A, 'Phase A'),
        (PHASE_B, 'Phase B'),
        (PHASE_C, 'Phase C'),
        (LINE_1, 'Line 1'),
        (LINE_2, 'Line 2'),
        (LINE_3, 'Line 3'),
    ]
