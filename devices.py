import pandas
import signals
import nass

AI_SIGNALS_HEADER_FRAME = signals.generate_header(signal_header_dict=signals.AI().header_attributes)
DI_SIGNALS_HEADER_FRAME = signals.generate_header(signal_header_dict=signals.DI().header_attributes)
AR_SIGNALS_HEADER_FRAME = signals.generate_header(signal_header_dict=signals.AR().header_attributes)
DR_SIGNALS_HEADER_FRAME = signals.generate_header(signal_header_dict=signals.DR().header_attributes)
DA_SIGNALS_HEADER_FRAME = signals.generate_header(signal_header_dict=signals.DA().header_attributes)


# FIXME : update 2 part tags to 3 part with XXX format
# FIXME : can change tag and add zsi or SI1 on the given part and have all 2 parts / tag 2 part for VFD and ss mixer
def frame_combiner(header_frame: pandas.DataFrame, frame_list: list) -> pandas.DataFrame:
    """ Takes the header_frame  and  the list of frames associated with The desired signal ,Return a Pandas Data Frame
     combining all the frame in the list with the appropriate header"""
    for frame in frame_list:
        header_frame = pandas.concat(
            [header_frame,
             signals.generate_signal_row(
                 signal_header_dict=frame.header_attributes,
                 signal_attributes_list=frame.attributes)],
            ignore_index=True
        )
    return header_frame


class PumpSS(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  SS Pump  and includes SS Pumps characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- SS Pump Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here ( Nothing on SS pump ) ---------- #
        # ---------- SS Pump - AI Signals ---------- #
        self.pumpss_ai_signals = [self.runtime_hours, self.start_counter_total,
                                  self.start_counter_today, self.start_counter_month]

        # ---------- SS Pump - DI Signals ---------- #
        self.pumpss_di_signals = [self.auto_mode, self.remote_mode, self.manual_mode,
                                  self.running_status, self.power_on_delay]

        # ---------- SS Pump - DR Signals ---------- #
        self.pumpss_dr_signals = [self.runtime_reset, self.out_service, self.manual_start_req, self.manual_stop_req,
                                  self.manual_mode_req, self.auto_mode_req, self.alarm_ack, self.backup_reset]

        # ---------- SS Pump - DA Signals ---------- #
        self.pumpss_da_signals = [self.fail_start_alarm, self.fail_stop_alarm, self.uncommand_start_alarm,
                                  self.uncommand_stop_alarm, self.general_alarm, self.start_float_alarm,
                                  self.on_float_alarm, self.soft_started_fault_alarm, self.temp_leak_alarm]

        # -------------------------------- SS Pump Signals in single Frame  ----------------------#
        self.pumpss_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.pumpss_ai_signals)
        self.pumpss_di_signals_frame = frame_combiner(DI_SIGNALS_HEADER_FRAME, self.pumpss_di_signals)
        self.pumpss_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.pumpss_dr_signals)
        self.pumpss_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.pumpss_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.pumpss_ai_signals_frame, self.pumpss_di_signals_frame,
                           self.pumpss_dr_signals_frame, self.pumpss_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_pumpss_frame_list(self):
        return [self.pumpss_ai_signals_frame,
                self.pumpss_di_signals_frame,
                self.pumpss_dr_signals_frame,
                self.pumpss_da_signals_frame, ]

    # FIXME : update CSV gen and path making / not working now
    def generate_pumpss_csv(self):
        for frame in self.frame_list:
            frame.to_csv("converted.csv", mode='a', index=False)


class PumpVFD(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  VFD Pump  and includes VFD Pumps characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- VFD Pump Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here ---------- #
        self.auto_mode = nass.AutoMode(tag, description, plc_name, channel_name, alarm_area,
                                       scan_time="3", alarm_enable="DISABLE", event_messages="DISABLE")
        self.remote_mode = nass.RemoteMode(tag, description, plc_name, channel_name, alarm_area,
                                           scan_time="3", alarm_enable="DISABLE", event_messages="DISABLE")
        self.manual_mode = nass.ManualMode(tag, description, plc_name, channel_name, alarm_area,
                                           scan_time="3", alarm_enable="DISABLE", event_messages="DISABLE")
        self.running_status = nass.RunningStatus(tag, description, plc_name, channel_name, alarm_area,
                                                 scan_time="3", alarm_enable="DISABLE", event_messages="DISABLE")
        self.runtime_reset = nass.RunTimeReset(tag, description, plc_name, channel_name, alarm_area,
                                               open_tag="DISABLE", close_tag="ENABLE", event_messages="ENABLE")
        self.fail_start_alarm = nass.FailToStartAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                      alarm_priority="High")
        self.general_alarm = nass.GeneralAlarm(tag, description, plc_name, channel_name, alarm_area,
                                               alarm_priority="High")
        self.fail_stop_alarm = nass.FailToStopAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                    alarm_priority="High")
        self.uncommand_start_alarm = nass.UncommandedStartAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                                alarm_priority="High")
        self.uncommand_stop_alarm = nass.UncommandedStopAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                              alarm_priority="High")
        self.temp_leak_alarm = nass.TempLeakageAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                     alarm_priority="High")
        self.speed_maintenance_mode_alarm = nass.SpeedMaintenanceAlarm(tag, description, plc_name, channel_name,
                                                                       alarm_area, alarm_priority="High")
        self.speed_dev_alarm = nass.SpeedDevAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                  alarm_priority="High")
        self.speed_signal_error_alarm = nass.SpeedSignalErrorAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                                   alarm_priority="High")
        self.speed_hi_alarm = nass.SpeedHiAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                alarm_priority="High")
        self.speed_hi_hi_alarm = nass.SpeedHiHiAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                     alarm_priority="High")
        self.speed_low_alarm = nass.SpeedLowAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                  alarm_priority="High")
        self.speed_low_low_alarm = nass.SpeedLowLowAlarm(tag, description, plc_name, channel_name, alarm_area,
                                                         alarm_priority="High")
        self.fault_alarm = nass.FAULTAlarm(tag, description, plc_name, channel_name, alarm_area,
                                           alarm_priority="High")
        # ---------- VFD Pump - AI Signals ---------- #
        self.pump_vfd_ai_signals = [self.runtime_hours, self.start_counter_total, self.start_counter_today,
                                    self.start_counter_month, self.speed_cv, self.speed_ma_value, self.speed_pct,
                                    self.speed_alarm_severity]

        # ---------- VFD Pump - DI Signals ---------- #
        self.pump_vfd_di_signals = [self.running_status, self.ready_status, self.auto_mode,
                                    self.manual_mode, self.remote_mode]

        # ---------- VFD Pump - AR Signals ---------- #
        self.pump_vfd_ar_signals = [self.hi_hi_setpoint, self.hi_setpoint, self.low_low_setpoint, self.low_setpoint,
                                    self.speed_deadband, self.centman_speed]

        # ---------- VFD Pump - DR Signals ---------- #
        self.pump_vfd_dr_signals = [self.runtime_reset, self.out_service, self.manual_start_req,
                                    self.manual_stop_req, self.manual_mode_req, self.auto_mode_req, self.alarm_ack,
                                    self.speed_hi_hi_alarm_enable, self.speed_hi_alarm_enable,
                                    self.speed_low_alarm_enable, self.speed_low_low_alarm_enable,
                                    self.maintenance_mode_enable]

        # ---------- VFD Pump - DA Signals ---------- #
        self.pump_vfd_da_signals = [self.fail_start_alarm, self.fail_stop_alarm,
                                    self.uncommand_start_alarm, self.speed_maintenance_mode_alarm,
                                    self.uncommand_stop_alarm, self.general_alarm,
                                    self.speed_dev_alarm, self.speed_hi_alarm,
                                    self.fault_alarm, self.speed_hi_hi_alarm,
                                    self.speed_low_alarm, self.speed_low_low_alarm,
                                    self.speed_signal_error_alarm, self.temp_leak_alarm]

        # -------------------------------- SS Pump Signals in single Frame  ----------------------#
        self.pump_vfd_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.pump_vfd_ai_signals)
        self.pump_vfd_di_signals_frame = frame_combiner(DI_SIGNALS_HEADER_FRAME, self.pump_vfd_di_signals)
        self.pump_vfd_ar_signals_frame = frame_combiner(AR_SIGNALS_HEADER_FRAME, self.pump_vfd_ar_signals)
        self.pump_vfd_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.pump_vfd_dr_signals)
        self.pump_vfd_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.pump_vfd_da_signals)
        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.pump_vfd_ai_signals_frame, self.pump_vfd_di_signals_frame,
                           self.pump_vfd_ar_signals_frame, self.pump_vfd_dr_signals_frame,
                           self.pump_vfd_da_signals_frame]

    # FIXME : temp till fix csv gen
    def gen_pump_vfd_frame_list(self):
        return [self.pump_vfd_ai_signals_frame,
                self.pump_vfd_di_signals_frame,
                self.pump_vfd_ar_signals_frame,
                self.pump_vfd_dr_signals_frame,
                self.pump_vfd_da_signals_frame, ]


# TODO : Check the differences
class PumpMixer(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  Mixer Pump  and includes Mixer Pumps characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- Mixer Pump Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here  ---------- #
        # ---------- Mixer Pump - AI Signals ---------- #
        self.mixer_pump_ai_signals = [self.runtime_hours, self.start_counter_total,
                                      self.start_counter_today, self.start_counter_month]

        # ---------- Mixer Pump - DI Signals ---------- #
        self.mixer_pump_di_signals = [self.auto_mode, self.remote_mode, self.manual_mode,
                                      self.running_status, self.ready_status]

        # ---------- Mixer Pump - DR Signals ---------- #
        self.mixer_pump_dr_signals = [self.runtime_reset, self.out_service, self.manual_start_req, self.manual_stop_req,
                                      self.manual_mode_req, self.alarm_ack]

        # ---------- Mixer Pump - DA Signals ---------- #
        self.mixer_pump_da_signals = [self.fail_start_alarm, self.fail_stop_alarm, self.uncommand_start_alarm,
                                      self.uncommand_stop_alarm, self.general_alarm, self.fault_alarm]

        # -------------------------------- Mixer Pump Signals in single Frame  ----------------------#
        self.mixer_pump_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.mixer_pump_ai_signals)
        self.mixer_pump_di_signals_frame = frame_combiner(DI_SIGNALS_HEADER_FRAME, self.mixer_pump_di_signals)
        self.mixer_pump_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.mixer_pump_dr_signals)
        self.mixer_pump_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.mixer_pump_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.mixer_pump_ai_signals_frame, self.mixer_pump_di_signals_frame,
                           self.mixer_pump_dr_signals_frame, self.mixer_pump_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_mixer_pump_frame_list(self):
        return [self.mixer_pump_ai_signals_frame,
                self.mixer_pump_di_signals_frame,
                self.mixer_pump_dr_signals_frame,
                self.mixer_pump_da_signals_frame, ]


# TODO : Check the differences
class FITransmitter(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  FIT type  Transmitter  and includes FIT characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- FIT Transmitter Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here  ---------- #
        # ---------- FIT Transmitter - AI Signals ---------- #
        self.fit_trans_ai_signals = [self.speed_cv, self.speed_ma_value, self.speed_pct, self.speed_alarm_severity,
                                     self.rate_ind_tot_today, self.rate_ind_tot_yesterday,
                                     self.rate_ind_tot_this_month, self.rate_ind_tot_last_month]

        # ---------- FIT Transmitter - AR Signals ---------- #
        self.fit_trans_ar_signals = [self.hi_hi_setpoint, self.hi_setpoint, self.low_low_setpoint,
                                     self.low_setpoint, self.speed_deadband, self.maintenance_time_var]

        # ---------- FIT Transmitter - DR Signals ---------- #
        self.fit_trans_dr_signals = [self.speed_hi_alarm_enable, self.speed_hi_hi_alarm_enable,
                                     self.speed_low_alarm_enable, self.speed_low_low_alarm_enable,
                                     self.maintenance_mode_enable, self.signal_error_enable, self.fault_alarm_enable]

        # ---------- FIT Transmitter - DA Signals ---------- #
        self.fit_trans_da_signals = [self.speed_hi_hi_alarm, self.speed_hi_alarm, self.speed_low_alarm,
                                     self.speed_low_low_alarm, self.speed_maintenance_mode_alarm,
                                     self.speed_signal_error_alarm, self.fault_alarm]

        # -------------------------------- FIT Transmitter Signals in single Frame  ----------------------#
        self.fit_trans_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.fit_trans_ai_signals)
        self.fit_trans_ar_signals_frame = frame_combiner(AR_SIGNALS_HEADER_FRAME, self.fit_trans_ar_signals)
        self.fit_trans_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.fit_trans_dr_signals)
        self.fit_trans_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.fit_trans_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.fit_trans_ai_signals_frame, self.fit_trans_ar_signals_frame,
                           self.fit_trans_dr_signals_frame, self.fit_trans_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_fit_trans_frame_list(self):
        return [self.fit_trans_ai_signals_frame,
                self.fit_trans_ar_signals_frame,
                self.fit_trans_dr_signals_frame,
                self.fit_trans_da_signals_frame, ]


# TODO : Check the differences
class LITransmitter(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  LIT type  Transmitter  and includes LIT characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- LIT Transmitter Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here  ---------- #
        # ---------- LIT Transmitter - AI Signals ---------- #
        self.lit_trans_ai_signals = [self.speed_cv, self.speed_ma_value, self.speed_pct, self.speed_alarm_severity, ]

        # ---------- LIT Transmitter - AR Signals ---------- #
        self.lit_trans_ar_signals = [self.hi_hi_setpoint, self.hi_setpoint, self.low_low_setpoint,
                                     self.low_setpoint, self.speed_deadband, self.maintenance_time_var]

        # ---------- LIT Transmitter - DR Signals ---------- #
        self.lit_trans_dr_signals = [self.speed_hi_alarm_enable, self.speed_hi_hi_alarm_enable, self.loe_enable,
                                     self.speed_low_alarm_enable, self.speed_low_low_alarm_enable,
                                     self.maintenance_mode_enable, self.signal_error_enable, self.fault_alarm_enable]

        # ---------- LIT Transmitter - DA Signals ---------- #
        self.lit_trans_da_signals = [self.speed_hi_hi_alarm, self.speed_hi_alarm, self.speed_low_alarm,
                                     self.speed_low_low_alarm, self.speed_maintenance_mode_alarm,
                                     self.speed_signal_error_alarm, self.loe_alarm]

        # -------------------------------- LIT Transmitter Signals in single Frame  ----------------------#
        self.lit_trans_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.lit_trans_ai_signals)
        self.lit_trans_ar_signals_frame = frame_combiner(AR_SIGNALS_HEADER_FRAME, self.lit_trans_ar_signals)
        self.lit_trans_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.lit_trans_dr_signals)
        self.lit_trans_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.lit_trans_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.lit_trans_ai_signals_frame, self.lit_trans_ar_signals_frame,
                           self.lit_trans_dr_signals_frame, self.lit_trans_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_lit_trans_frame_list(self):
        return [self.lit_trans_ai_signals_frame,
                self.lit_trans_ar_signals_frame,
                self.lit_trans_dr_signals_frame,
                self.lit_trans_da_signals_frame, ]


# TODO : Check the differences
class ValveGate(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  LIT type  Transmitter  and includes LIT characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- Valve Gate Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here  ---------- #
        # ---------- Valve Gate - DI Signals ---------- #
        self.valve_gate_di_signals = [self.remote_mode, self.manual_mode, self.auto_mode,
                                      self.open_status, self.close_status]

        # ---------- Valve Gate - DR Signals ---------- #
        self.valve_gate_dr_signals = [self.alarm_ack, self.manual_mode_req, self.manual_open_req,
                                      self.manual_close_req, self.runtime_reset, self.out_service]

        # ---------- Valve Gate - DA Signals ---------- #
        self.valve_gate_da_signals = [self.uncommand_close_alarm, self.uncommand_open_alarm, self.fail_open_alarm,
                                      self.fail_close_alarm, self.general_alarm, self.fault_alarm]

        # -------------------------------- Valve Gate Signals in single Frame  ----------------------#
        self.valve_gate_di_signals_frame = frame_combiner(DI_SIGNALS_HEADER_FRAME, self.valve_gate_di_signals)
        self.valve_gate_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.valve_gate_dr_signals)
        self.valve_gate_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.valve_gate_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.valve_gate_di_signals_frame, self.valve_gate_dr_signals_frame,
                           self.valve_gate_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_valve_gate_frame_list(self):
        return [self.valve_gate_di_signals_frame,
                self.valve_gate_dr_signals_frame,
                self.valve_gate_da_signals_frame, ]


# TODO : Check the differences
class GeneralTransmitter(nass.SCADAAlarms):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  General type  Transmitter  and includes LIT characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- General Transmitter Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here  ---------- #
        # ---------- General Transmitter - AI Signals ---------- #
        self.general_trans_ai_signals = [self.speed_cv, self.speed_ma_value, self.speed_pct,
                                         self.speed_alarm_severity, ]

        # ---------- General Transmitter - AR Signals ---------- #
        self.general_trans_ar_signals = [self.hi_hi_setpoint, self.hi_setpoint, self.low_low_setpoint,
                                         self.low_setpoint, self.speed_deadband, self.maintenance_time_var]

        # ---------- General Transmitter - DR Signals ---------- #
        self.general_trans_dr_signals = [self.speed_hi_alarm_enable, self.speed_hi_hi_alarm_enable, self.alarm_enable,
                                         self.speed_low_alarm_enable, self.speed_low_low_alarm_enable,
                                         self.maintenance_mode_enable, self.signal_error_enable]

        # ---------- General Transmitter - DA Signals ---------- #
        self.general_trans_da_signals = [self.speed_hi_hi_alarm, self.speed_hi_alarm, self.speed_low_alarm,
                                         self.speed_low_low_alarm, self.speed_maintenance_mode_alarm,
                                         self.speed_signal_error_alarm]

        # -------------------------------- General Transmitter Signals in single Frame  ----------------------#
        self.general_trans_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.general_trans_ai_signals)
        self.general_trans_ar_signals_frame = frame_combiner(AR_SIGNALS_HEADER_FRAME, self.general_trans_ar_signals)
        self.general_trans_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.general_trans_dr_signals)
        self.general_trans_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.general_trans_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.general_trans_ai_signals_frame, self.general_trans_ar_signals_frame,
                           self.general_trans_dr_signals_frame, self.general_trans_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_general_trans_frame_list(self):
        return [self.general_trans_ai_signals_frame,
                self.general_trans_ar_signals_frame,
                self.general_trans_dr_signals_frame,
                self.general_trans_da_signals_frame, ]


# TODO : Check the differences
class GeneralTransmitterHW(GeneralTransmitter):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is a  General type  Transmitter  and includes LIT characteristics """
        super().__init__(tag=tag, description=description, plc_name=plc_name, channel_name=channel_name,
                         alarm_area=alarm_area)
        # -------------------------------- General HW Transmitter Signals  ------------------------------------ #
        # ---------- Signals out of normal Standard will be modified here  ---------- #
        # ---------- General HW Transmitter - AI Signals ---------- #
        # ---------- General HW Transmitter - AR Signals ---------- #
        # ---------- General HW Transmitter - DR Signals ---------- #
        self.general_trans_dr_signals.append(self.fault_alarm_enable)

        # ---------- General HW Transmitter - DA Signals ---------- #
        self.general_trans_da_signals.append(self.fault_alarm)

        # -------------------------------- General HS Transmitter Signals in single Frame  ----------------------#
        self.hw_trans_ai_signals_frame = frame_combiner(AI_SIGNALS_HEADER_FRAME, self.general_trans_ai_signals)
        self.hw_trans_ar_signals_frame = frame_combiner(AR_SIGNALS_HEADER_FRAME, self.general_trans_ar_signals)
        self.hw_trans_dr_signals_frame = frame_combiner(DR_SIGNALS_HEADER_FRAME, self.general_trans_dr_signals)
        self.hw_trans_da_signals_frame = frame_combiner(DA_SIGNALS_HEADER_FRAME, self.general_trans_da_signals)

        # -------------------------------- List of all Signals frames  ------------------------#
        self.frame_list = [self.hw_trans_ai_signals_frame, self.hw_trans_ar_signals_frame,
                           self.hw_trans_dr_signals_frame, self.hw_trans_da_signals_frame, ]

    # FIXME : temp till fix csv gen
    def gen_hw_trans_frame_list(self):
        return [self.hw_trans_ai_signals_frame,
                self.hw_trans_ar_signals_frame,
                self.hw_trans_dr_signals_frame,
                self.hw_trans_da_signals_frame, ]
