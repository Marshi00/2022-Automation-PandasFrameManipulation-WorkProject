import signals

""" Store individual standard signals and combine all of them in a SCADA class at the end of this file
 for ease of access"""


# -------------------------------------- AI TYPE -------------------------------------- #
# ---------- Runtime Hours ---------- #
class RuntimeHours(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Run Time hours Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_RUNNI_HRS"
        self.description = f"{description} Runtime Hours"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.RUNNI_HRS"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "hrs")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- start Counter Total ---------- #
class StartCounterTotal(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Start Counter Total Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_STTOT_CRT"
        self.description = f"{description} Start Counter Total"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.STTOT_CRT.ACC"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "Starts")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Start Counter Today ---------- #
class StartCounterToday(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Start Counter Today Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_STTDY_CRT"
        self.description = f"{description} Start Counter Today"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.STTDY_CRT.ACC"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "Starts")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Start Counter Month ---------- #
class StartCounterMonth(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Start Counter Month Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_STMTH_CRT"
        self.description = f"{description} Start Counter Month"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.STMTH_CRT.ACC"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "Starts")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Rate Indicator Total Today ---------- #
class RateIndicatorTotalToday(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Rate Indicator Total Today Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_TOTAL_TDY"
        self.description = f"{description} Rate Ind. TOT Today"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.TOTAL_TDY"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "m3")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Rate Indicator Total Yesterday ---------- #
class RateIndicatorTotalYesterday(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Rate Indicator Total Yesterday Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_TOTAL_YTD"
        self.description = f"{description} Rate Ind. TOT Yesterday"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.TOTAL_YTD"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "m3")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Rate Indicator Total This Month ---------- #
class RateIndicatorTotalThisMonth(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Rate Indicator Total This Month Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_TOTAL_TMN"
        self.description = f"{description} Rate Ind. TOT This Month"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.TOTAL_TMN"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "m3")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Rate Indicator Total Last Month ---------- #
class RateIndicatorTotalLastMonth(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Rate Indicator Total Last Month Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_TOTAL_LMN"
        self.description = f"{description} Rate Ind. TOT Last Month"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.TOTAL_LMN"
        self.high_egu_limit = kwargs.get("high_egu_limit", "999,999")
        self.egu_tag = kwargs.get("egu_tag", "m3")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "999999")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "999999")
        self.dead_band = kwargs.get("dead_band", "50000")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "999999")
        self.attributes = signals.ai_col_list(self)


# ---------- Speed CV ---------- #
class SpeedCV(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed CV Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STAAI_CV"
        self.description = f"{description} Speed CV"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.CV"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "100")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "100")
        self.dead_band = kwargs.get("dead_band", "5")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "100")
        self.attributes = signals.ai_col_list(self)


# ---------- Speed mA Value ---------- #
class SpeedMAValue(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed mA Value Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STAAI_MA"
        self.description = f"{description} Speed mA Value"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.MA"
        self.low_egu_limit = kwargs.get("low_egu_limit", "4")
        self.high_egu_limit = kwargs.get("high_egu_limit", "20")
        self.egu_tag = kwargs.get("egu_tag", "mA")
        self.lo_alarm_limit = kwargs.get("lo_alarm_limit", "4")
        self.lo_lo_alarm_limit = kwargs.get("lo_lo_alarm_limit", "4")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "20")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "20")
        self.dead_band = kwargs.get("dead_band", "1")
        self.alarm_area_1 = alarm_area
        self.scale_low = kwargs.get("scale_low", "4")
        self.scale_high = kwargs.get("scale_high", "20")
        self.attributes = signals.ai_col_list(self)


# ---------- Speed PCT ---------- #
class SpeedPCT(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed PCT Value Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STAAI_PCT"
        self.description = f"{description} Speed PCT"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.PCT"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "100")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "100")
        self.dead_band = kwargs.get("dead_band", "5")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "100")
        self.attributes = signals.ai_col_list(self)


# ---------- Speed Alarm Severity ---------- #
class SpeedAlarmSeverity(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed Alarm Severity Signal - AI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_ALARM_SEV"
        self.description = f"{description} Speed Alarm Severity"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.ALARM_SEV"
        self.high_egu_limit = kwargs.get("high_egu_limit", "3")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "3")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "3")
        self.dead_band = kwargs.get("dead_band", "0")
        self.alarm_area_1 = alarm_area
        self.scale_high = kwargs.get("scale_high", "3")
        self.attributes = signals.ai_col_list(self)


# FIXME: Status Set !!
# -------------------------------------- DI TYPE -------------------------------------- #
# ---------- Auto Mode ---------- #
class AutoMode(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Auto Mode Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_ZS1_AUTOM_STS"
        self.description = f"{description} Auto Mode"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_AUTOM_STS"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "OTHER")
        self.close_tag = kwargs.get("close_tag", "AUTO")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.event_messages = kwargs.get("event_messages", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# ---------- Remote Mode ---------- #
class RemoteMode(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Remote Mode Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_ZS1_REMOT_STS"
        self.description = f"{description} Remote STS"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_REMOT_STS"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "LOCAL")
        self.close_tag = kwargs.get("close_tag", "REMOTE")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.event_messages = kwargs.get("event_messages", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# ---------- Remote Mode ---------- #
class ManualMode(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Manual Mode Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_ZS1_MANLM_STS"
        self.description = f"{description} Manual Mode"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_MANLM_STS"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "OTHER")
        self.close_tag = kwargs.get("close_tag", "MANUAL")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.event_messages = kwargs.get("event_messages", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# ---------- Running Status ---------- #
class RunningStatus(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Running Status Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_RUNNG_STS"
        self.description = f"{description} Running Status"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.RUNNG_STS"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "OFF")
        self.close_tag = kwargs.get("close_tag", "RUNNING")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.event_messages = kwargs.get("event_messages", "ENABLE")
        self.attributes = signals.di_col_list(self)


# ---------- Power On Delay ---------- #
class PowerOnDelay(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Power On Delay Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_RVS_HTALM_STS"
        self.description = f"{description} Power On Delay"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_RVS_HTALM_STS"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "OFF")
        self.close_tag = kwargs.get("close_tag", "ON")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.event_messages = kwargs.get("event_messages", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# ---------- Ready Status ---------- #
class ReadyStatus(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Ready Status Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_READY_STS"
        self.description = f"{description} Ready Status"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.AVBLE_STS"
        self.scan_time = kwargs.get("scan_time", "3")
        self.open_tag = kwargs.get("open_tag", "LOCAL")
        self.close_tag = kwargs.get("close_tag", "REMOTE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# ---------- Opened Status ---------- #
class OpenedStatus(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Opened Status Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_OPEND_STS"
        self.description = f"{description} Opened Status"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.OPEN_STS"
        self.scan_time = kwargs.get("scan_time", "3")
        self.open_tag = kwargs.get("open_tag", "CLOSED")
        self.close_tag = kwargs.get("close_tag", "OPENED")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# ---------- Closed Status ---------- #
class CloseStatus(signals.DI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Closed Status Signal - DI type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_CLOSE_STS"
        self.description = f"{description} Closed Status"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.CLOSE_STS"
        self.scan_time = kwargs.get("scan_time", "3")
        self.open_tag = kwargs.get("open_tag", "OPENED")
        self.close_tag = kwargs.get("close_tag", "CLOSED")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.di_col_list(self)


# FIXME: SPeed remove !!
# -------------------------------------- AR TYPE -------------------------------------- #
# ---------- Speed HI HI Set point ---------- #
class SpeedHiHiSetPoint(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed HI HI Set point Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SETPT_HH"
        self.description = f"{description} Speed HIHI Setpoint"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_HH"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.enable_output = kwargs.get("enable_output", "YES")
        self.attributes = signals.ar_col_list(self)


# ---------- Speed HI  Set point ---------- #
class SpeedHiSetPoint(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed HI  Set point Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SETPT_HI"
        self.description = f"{description} Speed HI Setpoint"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_HI"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.enable_output = kwargs.get("enable_output", "YES")
        self.attributes = signals.ar_col_list(self)


# ---------- Speed Low  Set point ---------- #
class SpeedLowSetPoint(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed Low  Set point Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SETPT_LO"
        self.description = f"{description} Speed LO Setpoint"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_LO"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.enable_output = kwargs.get("enable_output", "YES")
        self.attributes = signals.ar_col_list(self)


# ---------- Speed Low Low Set point ---------- #
class SpeedLowLowSetPoint(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed Low Low Set point Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SETPT_LL"
        self.description = f"{description} Speed LOLO Setpoint"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_LL"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.enable_output = kwargs.get("enable_output", "YES")
        self.attributes = signals.ar_col_list(self)


# ---------- Speed Deadband ---------- #
class SpeedDeadband(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed Deadband Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SIGDB_REQ"
        self.description = f"{description} Speed Deadband Setpoint"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SIGDB_REQ"
        self.high_egu_limit = kwargs.get("high_egu_limit", "1")
        self.scale_high = kwargs.get("scale_high", "1")
        self.attributes = signals.ar_col_list(self)


# ---------- Centman Speed ---------- #
class CentmanSpeed(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Centman Speed Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_SETPT_MAN"
        self.description = f"{description} Centman Speed"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.SETPT_MAN"
        self.high_egu_limit = kwargs.get("high_egu_limit", "100")
        self.egu_tag = kwargs.get("egu_tag", "%")
        self.enable_output = kwargs.get("enable_output", "YES")
        self.attributes = signals.ar_col_list(self)


# ---------- Maintenance time  variable ---------- #
class MaintenanceTimeVariable(signals.AR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Maintenance time  variable Signal - AR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_MAINT_VAR"
        self.description = f"{description} Maint. Time"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_MAINT_VAR"
        self.high_egu_limit = kwargs.get("high_egu_limit", "120")
        self.egu_tag = kwargs.get("egu_tag", "min")
        self.enable_output = kwargs.get("enable_output", "YES")
        self.attributes = signals.ar_col_list(self)


# -------------------------------------- DR TYPE -------------------------------------- #
# ---------- Run Time Reset ---------- #
class RunTimeReset(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Run Time Reset Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_RNTME_RST"
        self.description = f"{description} Run Time Reset"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.RNTME_RST"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OFF")
        self.close_tag = kwargs.get("close_tag", "RESET")
        self.attributes = signals.dr_col_list(self)


# ---------- Out of Service ---------- #
class OutOfService(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Out of Service Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_OUTSV_STS"
        self.description = f"{description} Out of Service"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_OUTSV_STS"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.event_messages = kwargs.get("event_messages", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ---------- Manual Start Request ---------- #
class ManualStartRequest(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Manual Start Request Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_MANST_REQ"
        self.description = f"{description} Manual Start Request"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.MANST_REQ"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OFF")
        self.close_tag = kwargs.get("close_tag", "START")
        self.attributes = signals.dr_col_list(self)


# ---------- Manual Stop Request ---------- #
class ManualStopRequest(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Manual Stop Request Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_MANSP_REQ"
        self.description = f"{description} Manual Stop Request"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.MANSP_REQ"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OFF")
        self.close_tag = kwargs.get("close_tag", "STOP")
        self.attributes = signals.dr_col_list(self)


# ---------- Manual Mode Request ---------- #
class ManualModeRequest(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Manual Mode Request Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_MANLM_REQ"
        self.description = f"{description} Manual Mode Request"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.MANLM_REQ"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "AUTO")
        self.close_tag = kwargs.get("close_tag", "MANUAL")
        self.attributes = signals.dr_col_list(self)


# ---------- Auto Mode Request ---------- #
class AutoModeRequest(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Auto Mode Request Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_AUTOM_REQ"
        self.description = f"{description} Auto Mode Request"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.AUTOM_REQ"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OPEN")
        self.close_tag = kwargs.get("close_tag", "CLOSE")
        self.attributes = signals.dr_col_list(self)


# ---------- Alarm Acknowledge ---------- #
class AlarmAcknowledge(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Alarm Acknowledge Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_ALARM_ACK"
        self.description = f"{description} Alarm Acknowledge"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ALARM_ACK"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OFF")
        self.close_tag = kwargs.get("close_tag", "ACK")
        self.attributes = signals.dr_col_list(self)


# ---------- Backup Reset ---------- #
class BackupReset(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Backup Reset Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_BCKUP_RST"
        self.description = f"{description} Backup Reset"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.BCKUP_RST"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OPEN")
        self.close_tag = kwargs.get("close_tag", "CLOSE")
        self.attributes = signals.dr_col_list(self)


# ---------- Speed HI HI Alarm Enable ---------- #
class SpeedHiHiAlarmEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard  Speed HI HI Alarm Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_HHALM_ENB"
        self.description = f"{description} Spd HIHI Alm EN"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.HHALM_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ---------- Speed HI Alarm Enable ---------- #
class SpeedHiAlarmEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed HI Alarm Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_HIALM_ENB"
        self.description = f"{description} Spd HI Alm EN"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.HIALM_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ---------- Speed Low Low  Alarm Enable ---------- #
class SpeedLowLowAlarmEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Low Low  Alarm Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_LLALM_ENB"
        self.description = f"{description} Spd LOLO Alm EN"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.LLALM_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ---------- Speed Low  Alarm Enable ---------- #
class SpeedLowAlarmEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American  Standard Speed Low Alarm Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_LOALM_ENB"
        self.description = f"{description} Spd LO Alm EN"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.LOALM_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ---------- Speed Maintenance Mode Enable ---------- #
class SpeedMaintenanceModeEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Maintenance Mode Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_MAINT_ENB"
        self.description = f"{description} Spd Maint Mode En"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.MAINT_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ----------  Signal Error Enable ---------- #
class SignalErrorEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard  Signal Error Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SIGNL_ENB"
        self.description = f"{description}  Signal Error En"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.SIGNL_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ----------  Fault Alarm Enable ---------- #
class FaultAlarmEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard  Fault Alarm Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_FAULT_ENB"
        self.description = f"{description}  Fault Alarm En"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_FAULT_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ----------  Alarm Enable ---------- #
class AlarmEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard  Alarm Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_ALARM_ENB"
        self.description = f"{description} Alarm En"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ALARM_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ----------  LOE Enable ---------- #
class LOEEnable(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard  LOE Enable Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_LECHO_ENB"
        self.description = f"{description} LOE En"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_LOE_ENB"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "DISABLE")
        self.close_tag = kwargs.get("close_tag", "ENABLE")
        self.attributes = signals.dr_col_list(self)


# ----------  Manual Open REQ ---------- #
class ManualOpenReq(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Manual OPEN REQ Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_MANOP_REQ"
        self.description = f"{description} Manual Open Req"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.MANOPN_REQ"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "OPEN")
        self.close_tag = kwargs.get("close_tag", "CLOSE")
        self.attributes = signals.dr_col_list(self)


# ----------  Manual CLOSE REQ ---------- #
class ManualCloseReq(signals.DR):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Manual CLOSE REQ Signal - DR type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_MANCL_REQ"
        self.description = f"{description} Manual Close Req"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.MANCLS_REQ"
        self.enable_output = kwargs.get("enable_output", "YES")
        self.open_tag = kwargs.get("open_tag", "CLOSE")
        self.close_tag = kwargs.get("close_tag", "OPEN")
        self.attributes = signals.dr_col_list(self)


# -------------------------------------- DA TYPE -------------------------------------- #
# ---------- Fail To Start Alarm ---------- #
class FailToStartAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Fail To Start Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_FLSTR_ALM"
        self.description = f"{description} Fail To Start Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.FLSTR_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


class FailToOpenAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Fail To Open Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_FLOPN_ALM"
        self.description = f"{description} Fail To open Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.FLOPN_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


class FailToCloseAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Fail To Close Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_FLCLS_ALM"
        self.description = f"{description} Fail To close Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.FLCLS_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Fail To Stop Alarm ---------- #
class FailToStopAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American StandardFail To Stop Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_FLSTP_ALM"
        self.description = f"{description} Fail To Stop Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.FLSTP_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Uncommanded Start Alarm ---------- #
class UncommandedStartAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Uncommanded Start Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_UCSTR_ALM"
        self.description = f"{description} Uncommand. Start Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.UCSTR_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Uncommanded Stop Alarm ---------- #
class UncommandedStopAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Uncommanded Stop Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_UCSTP_ALM"
        self.description = f"{description} Uncommand. Stop Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.UCSTP_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Uncommanded OPEN Alarm ---------- #
class UncommandedOpenAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Uncommanded open Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_UCOPN_ALM"
        self.description = f"{description} Uncommand. open Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.UCOPN_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Uncommanded close Alarm ---------- #
class UncommandedCloseAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Uncommanded Close Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_UCCLS_ALM"
        self.description = f"{description} Uncommand. close Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.UCCLS_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- General Alarm ---------- #
class GeneralAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard General Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_GENAL_ALM"
        self.description = f"{description} General Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.GENAL_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Start Float Alarm ---------- #
class StartFloatAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Start Float Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_SRTLS_ALM"
        self.description = f"{description} Start Float Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.SRTLS_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- ON Float Alarm ---------- #
class OnFloatAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard ON Float Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_ONFLT_ALM"
        self.description = f"{description} On Float Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.ONFLT_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Soft Starter Fault Alarm ---------- #
class SoftStarterFaultAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Soft Starter Fault Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_RVS_FAULT_ALM"
        self.description = f"{description} Soft Starter Fault Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.FAULT_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Temp/Leakage Alarm ---------- #
class TempLeakageAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Temp/Leakage Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_TMPLK_ALM"
        self.description = f"{description} Temp/Leakage Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.TMPLK_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Speed Dev Alarm ---------- #
class SpeedDevAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Dev Alarm Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_SPDDV_ALM"
        self.description = f"{description} Speed Dev Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.SPDDV_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ----------  FAULT Alarm  ---------- #
class FAULTAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard VFD FAULT Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_FAULT_ALM"
        self.description = f"{description} Fault Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.FAULT_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# FIXME : remove speed !
# ---------- Speed HI HI Alarm  ---------- #
class SpeedHiHiAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed HI HI Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STAHH_ALM"
        self.description = f"{description} Speed HIHI Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STAHH_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Speed HI  Alarm  ---------- #
class SpeedHiAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed HI  Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STAHI_ALM"
        self.description = f"{description} Speed HI Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STAHI_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Speed Low Low Alarm  ---------- #
class SpeedLowLowAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Low Low  Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STALL_ALM"
        self.description = f"{description} Speed LOLO Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STALL_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Speed Low Alarm  ---------- #
class SpeedLowAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Low Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_STALO_ALM"
        self.description = f"{description} Speed LO Alarm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STALO_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Speed Maintenance Alarm  ---------- #
class SpeedMaintenanceAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Maintenance Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_MAINT_ALM"
        self.description = f"{description} Spd Maint Mode Alm"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.MAINT_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- Speed Signal Error Alarm  ---------- #
class SpeedSignalErrorAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard Speed Signal Error Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SIGNL_ALM"
        self.description = f"{description} Speed Signal Error"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SIGNL_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.attributes = signals.da_col_list(self)


# ---------- LOE Alarm  ---------- #
class LOEAlarm(signals.DA):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ North American Standard LOE Alarm  Signal - DA type signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_SI1_SIGNL_ALM"
        self.description = f"{description} Speed Signal Error"
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}_LOE_ALM"
        self.scan_time = kwargs.get("scan_time", "10")
        self.open_tag = kwargs.get("open_tag", "NORMAL")
        self.close_tag = kwargs.get("close_tag", "ALARM")
        self.alarm_enable = kwargs.get("alarm_enable", "ENABLE")
        self.alarm_area_1 = alarm_area
        self.alarm_priority = "High"
        self.attributes = signals.da_col_list(self)


class SCADAAlarms:
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This Class Contains all the Standard Supervisory control and data acquisition System related Alarms,
         all devices inherit the standard alarms from here"""
        self.runtime_hours = RuntimeHours(tag, description, plc_name, channel_name, alarm_area)
        self.start_counter_total = StartCounterTotal(tag, description, plc_name, channel_name, alarm_area)
        self.start_counter_today = StartCounterToday(tag, description, plc_name, channel_name, alarm_area)
        self.start_counter_month = StartCounterMonth(tag, description, plc_name, channel_name, alarm_area)
        self.auto_mode = AutoMode(tag, description, plc_name, channel_name, alarm_area)
        self.remote_mode = RemoteMode(tag, description, plc_name, channel_name, alarm_area)
        self.manual_mode = ManualMode(tag, description, plc_name, channel_name, alarm_area)
        self.running_status = RunningStatus(tag, description, plc_name, channel_name, alarm_area)
        self.power_on_delay = PowerOnDelay(tag, description, plc_name, channel_name, alarm_area)
        self.runtime_reset = RunTimeReset(tag, description, plc_name, channel_name, alarm_area)
        self.out_service = OutOfService(tag, description, plc_name, channel_name, alarm_area)
        self.manual_start_req = ManualStartRequest(tag, description, plc_name, channel_name, alarm_area)
        self.manual_stop_req = ManualStopRequest(tag, description, plc_name, channel_name, alarm_area)
        self.manual_mode_req = ManualModeRequest(tag, description, plc_name, channel_name, alarm_area)
        self.auto_mode_req = AutoModeRequest(tag, description, plc_name, channel_name, alarm_area)
        self.alarm_ack = AlarmAcknowledge(tag, description, plc_name, channel_name, alarm_area)
        self.backup_reset = BackupReset(tag, description, plc_name, channel_name, alarm_area)
        self.fail_start_alarm = FailToStartAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.general_alarm = GeneralAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.fail_stop_alarm = FailToStopAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.uncommand_start_alarm = UncommandedStartAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.uncommand_stop_alarm = UncommandedStopAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.start_float_alarm = StartFloatAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.on_float_alarm = OnFloatAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.soft_started_fault_alarm = SoftStarterFaultAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.temp_leak_alarm = TempLeakageAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.speed_cv = SpeedCV(tag, description, plc_name, channel_name, alarm_area)
        self.speed_ma_value = SpeedMAValue(tag, description, plc_name, channel_name, alarm_area)
        self.speed_pct = SpeedPCT(tag, description, plc_name, channel_name, alarm_area)
        self.speed_alarm_severity = SpeedAlarmSeverity(tag, description, plc_name, channel_name, alarm_area)
        self.ready_status = ReadyStatus(tag, description, plc_name, channel_name, alarm_area)
        self.hi_hi_setpoint = SpeedHiHiSetPoint(tag, description, plc_name, channel_name, alarm_area)
        self.hi_setpoint = SpeedHiSetPoint(tag, description, plc_name, channel_name, alarm_area)
        self.low_low_setpoint = SpeedLowLowSetPoint(tag, description, plc_name, channel_name, alarm_area)
        self.low_setpoint = SpeedLowSetPoint(tag, description, plc_name, channel_name, alarm_area)
        self.speed_deadband = SpeedDeadband(tag, description, plc_name, channel_name, alarm_area)
        self.centman_speed = CentmanSpeed(tag, description, plc_name, channel_name, alarm_area)
        self.speed_hi_hi_alarm_enable = SpeedHiHiAlarmEnable(tag, description, plc_name, channel_name, alarm_area)
        self.speed_hi_alarm_enable = SpeedHiAlarmEnable(tag, description, plc_name, channel_name, alarm_area)
        self.speed_low_low_alarm_enable = SpeedLowLowAlarmEnable(tag, description, plc_name, channel_name,
                                                                 alarm_area)
        self.speed_low_alarm_enable = SpeedLowAlarmEnable(tag, description, plc_name, channel_name, alarm_area)
        self.maintenance_mode_enable = SpeedMaintenanceModeEnable(tag, description, plc_name, channel_name,
                                                                  alarm_area)
        self.speed_maintenance_mode_alarm = SpeedMaintenanceAlarm(tag, description, plc_name, channel_name,
                                                                  alarm_area)
        self.speed_dev_alarm = SpeedDevAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.speed_signal_error_alarm = SpeedSignalErrorAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.speed_hi_alarm = SpeedHiAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.speed_hi_hi_alarm = SpeedHiHiAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.speed_low_alarm = SpeedLowAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.speed_low_low_alarm = SpeedLowLowAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.fault_alarm = FAULTAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.rate_ind_tot_today = RateIndicatorTotalToday(tag, description, plc_name, channel_name, alarm_area)
        self.rate_ind_tot_yesterday = RateIndicatorTotalYesterday(tag, description, plc_name, channel_name, alarm_area)
        self.rate_ind_tot_this_month = RateIndicatorTotalThisMonth(tag, description, plc_name, channel_name, alarm_area)
        self.rate_ind_tot_last_month = RateIndicatorTotalLastMonth(tag, description, plc_name, channel_name, alarm_area)
        self.signal_error_enable = SignalErrorEnable(tag, description, plc_name, channel_name, alarm_area)
        self.fault_alarm_enable = FaultAlarmEnable(tag, description, plc_name, channel_name, alarm_area)
        self.maintenance_time_var = MaintenanceTimeVariable(tag, description, plc_name, channel_name, alarm_area)
        self.alarm_enable = AlarmEnable(tag, description, plc_name, channel_name, alarm_area)
        self.loe_enable = LOEEnable(tag, description, plc_name, channel_name, alarm_area)
        self.loe_alarm = LOEAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.open_status = OpenedStatus(tag, description, plc_name, channel_name, alarm_area)
        self.close_status = CloseStatus(tag, description, plc_name, channel_name, alarm_area)
        self.manual_open_req = ManualOpenReq(tag, description, plc_name, channel_name, alarm_area)
        self.manual_close_req = ManualCloseReq(tag, description, plc_name, channel_name, alarm_area)
        self.uncommand_open_alarm = UncommandedOpenAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.uncommand_close_alarm = UncommandedCloseAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.fail_open_alarm = FailToOpenAlarm(tag, description, plc_name, channel_name, alarm_area)
        self.fail_close_alarm = FailToCloseAlarm(tag, description, plc_name, channel_name, alarm_area)
