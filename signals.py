import pandas

# Todo Move to Debug file Later
import functools
import time


def debug_decorator(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


# Todo Move to Debug file Later
def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def generate_header(signal_header_dict: dict) -> pandas.DataFrame:
    """ Takes the header_attributes associated with The signal and Return a Pandas Data Frame with the format
        of { key : [value],} for the appropriate  Signal"""

    header_dict = {key: [value] for (key, value) in signal_header_dict.items()}
    return pandas.DataFrame(header_dict)


def generate_signal_row(signal_header_dict: dict, signal_attributes_list: list) -> pandas.DataFrame:
    """ Takes the attributes associated with a signal and Return a Pandas Data Frame with the format
                of { key : [value],} for the appropriate  Signal"""
    attributes_dict = {key: [value] for key, value in
                       zip([key for key in signal_header_dict], signal_attributes_list)}
    return pandas.DataFrame(attributes_dict)


class Signal:
    def __init__(self, **kwargs):
        """ This is a Starting Base of Signal  and includes shared variables in the format of { description,
        Tag name } - Notes: in order to follow naming convention 1: caps --> lowers 2: space --> _ 3: / --> _ """
        # -------------------------------- Signal Shared Attributes ------------------------------------ #
        self.block_type = kwargs.get("block_type", "")
        self.tag = kwargs.get("tag", "XXX_XXX1")
        self.description = kwargs.get("description", "XXXDESC")
        self.i_o_device = kwargs.get("i_o_device", "IGS")
        self.h_w_options = kwargs.get("h_w_options", "")
        self.i_o_address = kwargs.get("i_o_address", "CHXXX.XXXPLC01.XXX_XXX1")
        self.security_area_1 = kwargs.get("security_area_1", "NONE")
        self.security_area_2 = kwargs.get("security_area_2", "NONE")
        self.security_area_3 = kwargs.get("security_area_3", "NONE")
        self.user_field_1 = kwargs.get("user_field_1", "")
        self.user_field_2 = kwargs.get("user_field_2", "")
        self.esig_type = kwargs.get("esig_type", "NONE")
        self.esig_allow_cont_use = kwargs.get("esig_allow_cont_use", "YES")
        self.esig_xmpt_alarm_ack = kwargs.get("esig_xmpt_alarm_ack", "NO")
        self.esig_unsigned_writes = kwargs.get("esig_unsigned_writes", "REJECT")
        self.pdr_update_rate = kwargs.get("pdr_update_rate", "1000")
        self.pdr_access_time = kwargs.get("pdr_access_time", "300000")
        self.pdr_deadband = kwargs.get("pdr_deadband", "0")
        self.pdr_latch = kwargs.get("pdr_latch", "NO")
        self.pdr_disable_output = kwargs.get("pdr_disable_output", "NO")
        self.pdr_array_length = kwargs.get("pdr_array_length", "0")
        self.hist_description = kwargs.get("hist_description", "")
        self.hist_collect = kwargs.get("hist_collect", "NO")
        self.hist_interval = kwargs.get("hist_interval", "5000")
        self.hist_offset = kwargs.get("hist_offset", "0")
        self.hist_time_res = kwargs.get("hist_time_res", "Milliseconds")
        self.hist_compress = kwargs.get("hist_compress", "DISABLE")
        self.hist_deadband = kwargs.get("hist_deadband", "0")
        self.hist_comp_type = kwargs.get("hist_comp_type", "Absolute")
        self.hist_comp_time = kwargs.get("hist_comp_time", "0")
        self.enable_output = kwargs.get("enable_output", "NO")
        # -------------------------------- Signal Shared Headers ------------------------------------ #
        self.block_type_header = kwargs.get("block_type_header", {"[BLOCK TYPE": "!A_NAME"})
        self.tag_header = kwargs.get("tag_header", {"TAG": "A_TAG"})
        self.description_header = kwargs.get("description_header", {"DESCRIPTION": "A_DESC"})
        self.i_o_device_header = kwargs.get("i_o_device_header", {"I/O DEVICE": "A_IODV"})
        self.h_w_options_header = kwargs.get("h_w_options_header", {"H/W OPTIONS": "A_IOHT"})
        self.i_o_address_header = kwargs.get("i_o_address_header", {"I/O ADDRESS": "A_IOAD"})
        self.security_area_1_header = kwargs.get("security_area_1_header", {"SECURITY AREA 1": "A_SA1"})
        self.security_area_2_header = kwargs.get("security_area_2_header", {"SECURITY AREA 2": "A_SA2"})
        self.security_area_3_header = kwargs.get("security_area_3_header", {"SECURITY AREA 3": "A_SA3"})
        self.user_field_1_header = kwargs.get("user_field_1_header", {"USER FIELD 1": "A_ALMEXT1"})
        self.user_field_2_header = kwargs.get("user_field_2_header", {"USER FIELD 2": "A_ALMEXT2"})
        self.esig_type_header = kwargs.get("esig_type_header", {"ESIG TYPE": "A_ESIGTYPE"})
        self.esig_allow_cont_use_header = kwargs.get("esig_allow_cont_use_header",
                                                     {"ESIG ALLOW CONT USE": "A_ESIGCONT"})
        self.esig_xmpt_alarm_ack_header = kwargs.get("esig_xmpt_alarm_ack_header", {"ESIG XMPT ALARM ACK": "A_ESIGACK"})
        self.esig_unsigned_writes_header = kwargs.get("esig_unsigned_writes_header",
                                                      {"ESIG UNSIGNED WRITES": "A_ESIGTRAP"})
        self.pdr_update_rate_header = kwargs.get("pdr_update_rate_header", {"PDR Update Rate": "A_PDR_UPDATERATE"})
        self.pdr_access_time_header = kwargs.get("pdr_access_time_header", {"PDR Access Time": "A_PDR_ACCESSTIME"})
        self.pdr_deadband_header = kwargs.get("pdr_deadband_header", {"PDR Deadband": "A_PDR_DEADBAND"})
        self.pdr_latch_header = kwargs.get("pdr_latch_header", {"PDR Latch": "A_PDR_LATCHDATA"})
        self.pdr_disable_output_header = kwargs.get("pdr_disable_output_header",
                                                    {"PDR Disable Output": "A_PDR_DISABLEOUT"})
        self.pdr_array_length_header = kwargs.get("pdr_array_length_header", {"PDR Array Length": "A_PDR_ARRAYLENGTH"})
        self.hist_description_header = kwargs.get("hist_description_header", {"Hist Description": "A_HIST_DESC"})
        self.hist_collect_header = kwargs.get("hist_collect_header", {"Hist Collect": "A_HIST_COLLECT"})
        self.hist_interval_header = kwargs.get("hist_interval_header", {"Hist Interval": "A_HIST_INTERVAL"})
        self.hist_offset_header = kwargs.get("hist_offset_header", {"Hist Offset": "A_HIST_OFFSET"})
        self.hist_time_res_header = kwargs.get("hist_time_res_header", {"Hist Time Res": "A_HIST_TIMERES"})
        self.hist_compress_header = kwargs.get("hist_compress_header", {"Hist Compress": "A_HIST_COMPRESS"})
        self.hist_deadband_header = kwargs.get("hist_deadband_header", {"Hist Deadband": "A_HIST_DEADBAND"})
        self.hist_comp_type_header = kwargs.get("hist_comp_type_header", {"Hist Comp Type": "A_HIST_COMPTYPE"})
        self.hist_comp_time_header = kwargs.get("hist_comp_time_header", {"Hist Comp Time": "A_HIST_COMPTIME"})
        self.enable_output_header = kwargs.get("enable_output_header", {"ENABLE OUTPUT": "A_EOUT"})


class FeedBackSignal(Signal):
    def __init__(self, **kwargs):
        """ This is  FeedBackSignal type signals ( AI - DI - DA )   -  shared  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- FeedBackSignal Shared Attributes ------------------------------------ #
        self.alarm_area_1 = kwargs.get("alarm_area_1", "")
        self.alarm_area_2 = kwargs.get("alarm_area_2", "")
        self.alarm_area_3 = kwargs.get("alarm_area_3", "")
        self.alarm_area_4 = kwargs.get("alarm_area_4", "")
        self.alarm_area_5 = kwargs.get("alarm_area_5", "")
        self.alarm_area_6 = kwargs.get("alarm_area_6", "")
        self.alarm_area_7 = kwargs.get("alarm_area_7", "")
        self.alarm_area_8 = kwargs.get("alarm_area_8", "")
        self.alarm_area_9 = kwargs.get("alarm_area_9", "")
        self.alarm_area_9 = kwargs.get("alarm_area_9", "")
        self.alarm_area_10 = kwargs.get("alarm_area_10", "")
        self.alarm_area_11 = kwargs.get("alarm_area_11", "")
        self.alarm_area_12 = kwargs.get("alarm_area_12", "")
        self.alarm_area_13 = kwargs.get("alarm_area_13", "")
        self.alarm_area_14 = kwargs.get("alarm_area_14", "")
        self.alarm_area_15 = kwargs.get("alarm_area_15", "")
        self.initial_scan = kwargs.get("initial_scan", "ON")
        self.scan_time = kwargs.get("scan_time", "")
        self.initial_a_m_status = kwargs.get("initial_a_m_status", "AUTO")
        self.alarm_enable = kwargs.get("alarm_enable", "DISABLE")
        self.alarm_area_s = kwargs.get("alarm_area_s", "NONE")
        self.alarm_priority = kwargs.get("alarm_priority", "LOW")
        self.next_block = kwargs.get("next_block", "")
        # -------------------------------- FeedBackSignal Shared Headers ------------------------------------ #
        self.alarm_area_1_header = kwargs.get("alarm_area_1_header", {"ALARM AREA 1": "A_AREA1"})
        self.alarm_area_2_header = kwargs.get("alarm_area_2_header", {"ALARM AREA 2": "A_AREA2"})
        self.alarm_area_3_header = kwargs.get("alarm_area_3_header", {"ALARM AREA 3": "A_AREA3"})
        self.alarm_area_4_header = kwargs.get("alarm_area_4_header", {"ALARM AREA 4": "A_AREA4"})
        self.alarm_area_5_header = kwargs.get("alarm_area_5_header", {"ALARM AREA 5": "A_AREA5"})
        self.alarm_area_6_header = kwargs.get("alarm_area_6_header", {"ALARM AREA 6": "A_AREA6"})
        self.alarm_area_7_header = kwargs.get("alarm_area_7_header", {"ALARM AREA 7": "A_AREA7"})
        self.alarm_area_8_header = kwargs.get("alarm_area_8_header", {"ALARM AREA 8": "A_AREA8"})
        self.alarm_area_9_header = kwargs.get("alarm_area_9_header", {"ALARM AREA 9": "A_AREA9"})
        self.alarm_area_10_header = kwargs.get("alarm_area_10_header", {"ALARM AREA 10": "A_AREA10"})
        self.alarm_area_11_header = kwargs.get("alarm_area_11_header", {"ALARM AREA 11": "A_AREA11"})
        self.alarm_area_12_header = kwargs.get("alarm_area_12_header", {"ALARM AREA 12": "A_AREA12"})
        self.alarm_area_13_header = kwargs.get("alarm_area_13_header", {"ALARM AREA 13": "A_AREA13"})
        self.alarm_area_14_header = kwargs.get("alarm_area_14_header", {"ALARM AREA 14": "A_AREA14"})
        self.alarm_area_15_header = kwargs.get("alarm_area_15_header", {"ALARM AREA 15": "A_AREA15"})
        self.initial_scan_header = kwargs.get("initial_scan_header", {"INITIAL SCAN": "A_ISCAN"})
        self.scan_time_header = kwargs.get("scan_time_header", {"SCAN TIME": "A_SCANT"})
        self.initial_a_m_status_header = kwargs.get("initial_a_m_status_header", {"INITIAL A/M STATUS": "A_IAM"})
        self.alarm_enable_header = kwargs.get("alarm_enable_header", {"ALARM ENABLE": "A_IENAB"})
        self.alarm_area_s_header = kwargs.get("alarm_area_s_header", {"ALARM AREA(S)": "A_ADI"})
        self.alarm_priority_header = kwargs.get("alarm_priority_header", {"ALARM PRIORITY": "A_PRI"})
        self.next_block_header = kwargs.get("next_block_header", {"NEXT BLK": "A_NEXT"})


class ScalableSignal(Signal):
    def __init__(self, **kwargs):
        """ This is  Scalable Signal type signals ( AI - AR )   -  shared  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- ScalableSignal Shared Attributes ------------------------------------ #
        self.signal_conditioning = kwargs.get("signal_conditioning", "None")
        self.low_egu_limit = kwargs.get("low_egu_limit", "0")
        self.high_egu_limit = kwargs.get("high_egu_limit", "0")
        self.egu_tag = kwargs.get("egu_tag", "")
        self.scale_enabled = kwargs.get("scale_enabled", "NO")
        self.scale_clamping = kwargs.get("scale_clamping", "NO")
        self.scale_use_egu = kwargs.get("scale_use_egu", "YES")
        self.scale_raw_low = kwargs.get("scale_raw_low", "0")
        self.scale_raw_high = kwargs.get("scale_raw_high", "65535")
        self.scale_low = kwargs.get("scale_low", "0")
        self.scale_high = kwargs.get("scale_high", "100")
        # -------------------------------- ScalableSignal Shared Headers ------------------------------------ #
        self.signal_conditioning_header = kwargs.get("signal_conditioning_header", {"SIGNAL CONDITIONING": "A_IOSC"})
        self.low_egu_limit_header = kwargs.get("low_egu_limit_header", {"LOW EGU LIMIT": "A_ELO"})
        self.high_egu_limit_header = kwargs.get("high_egu_limit_header", {"HIGH EGU LIMIT": "A_EHI"})
        self.egu_tag_header = kwargs.get("egu_tag_header", {"EGU TAG": "A_EGUDESC"})
        self.scale_enabled_header = kwargs.get("scale_enabled_header", {"Scale Enabled": "A_SCALE_ENABLED"})
        self.scale_clamping_header = kwargs.get("scale_clamping_header", {"Scale Clamping": "A_SCALE_CLAMP"})
        self.scale_use_egu_header = kwargs.get("scale_use_egu_header", {"Scale Use EGU": "A_SCALE_USEEGU"})
        self.scale_raw_low_header = kwargs.get("scale_raw_low_header", {"Scale Raw Low": "A_SCALE_RAWLOW"})
        self.scale_raw_high_header = kwargs.get("scale_raw_high_header", {"Scale Raw High": "A_SCALE_RAWHIGH"})
        self.scale_low_header = kwargs.get("scale_low_header", {"Scale Low": "A_SCALE_LOW"})
        self.scale_high_header = kwargs.get("scale_high_header", {"Scale High]": "A_SCALE_HIGH!"})


class SingleBitSignals(Signal):
    def __init__(self, **kwargs):
        """This is for bit input type signals ( DI - DR - DA ) - Shared   characteristics """
        super().__init__(**kwargs)
        # -------------------------------- BitSignals Shared Attributes ------------------------------------ #
        self.invert_output = kwargs.get("invert_output", "NO")
        self.open_tag = kwargs.get("open_tag", "")
        self.close_tag = kwargs.get("close_tag", "")
        # -------------------------------- BitSignals Shared Headers ------------------------------------ #
        self.invert_output_header = kwargs.get("invert_output_header", {"INVERT OUTPUT": "A_INV"})
        self.open_tag_header = kwargs.get("open_tag_header", {"OPEN TAG": "A_OPENDESC"})
        self.close_tag_header = kwargs.get("close_tag_header", {"CLOSE TAG": "A_CLOSEDESC"})


class AI(FeedBackSignal, ScalableSignal):
    def __init__(self, **kwargs):
        """ This is  AI type signal  -  individual  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- AI Individual Attributes ------------------------------------ #
        self.block_type = kwargs.get("block_type", "AI")
        self.scan_time = kwargs.get("scan_time", "10")
        self.smoothing = kwargs.get("smoothing", "0")
        self.lo_lo_alarm_limit = kwargs.get("lo_lo_alarm_limit", "0")
        self.lo_alarm_limit = kwargs.get("lo_alarm_limit", "0")
        self.hi_alarm_limit = kwargs.get("hi_alarm_limit", "100")
        self.hi_hi_alarm_limit = kwargs.get("hi_hi_alarm_limit", "100")
        self.roc_alarm_limit = kwargs.get("roc_alarm_limit", "0")
        self.dead_band = kwargs.get("dead_band", "0")
        # -------------------------------- AI Individual Headers ------------------------------------ #
        self.smoothing_header = kwargs.get("smoothing_header", {"SMOOTHING": "A_SMOTH"})
        self.lo_lo_alarm_limit_header = kwargs.get("lo_lo_alarm_limit_header", {"LO LO ALARM LIMIT": "A_LOLO"})
        self.lo_alarm_limit_header = kwargs.get("lo_alarm_limit_header", {"LO ALARM LIMIT": "A_LO"})
        self.hi_alarm_limit_header = kwargs.get("hi_alarm_limit_header", {"HI ALARM LIMIT": "A_HI"})
        self.hi_hi_alarm_limit_header = kwargs.get("hi_hi_alarm_limit_header", {"HI HI ALARM LIMIT": "A_HIHI"})
        self.roc_alarm_limit_header = kwargs.get("roc_alarm_limit_header", {"ROC ALARM LIMIT": "A_ROC"})
        self.dead_band_header = kwargs.get("dead_band_header", {"DEAD BAND": "A_DBAND"})
        # -------------------------------- AI List  ------------------------------------ #
        self.attributes = ai_col_list(self)
        # -------------------------------- AI Dictionary ------------------------------------ #
        self.header_attributes = {**self.block_type_header, **self.tag_header, **self.next_block_header,
                                  **self.description_header, **self.initial_scan_header,
                                  **self.scan_time_header, **self.smoothing_header, **self.i_o_device_header,
                                  **self.h_w_options_header, **self.i_o_address_header,
                                  **self.signal_conditioning_header, **self.low_egu_limit_header,
                                  **self.high_egu_limit_header, **self.egu_tag_header,
                                  **self.initial_a_m_status_header,
                                  **self.alarm_enable_header, **self.alarm_area_s_header,
                                  **self.lo_lo_alarm_limit_header,
                                  **self.lo_alarm_limit_header, **self.hi_alarm_limit_header,
                                  **self.hi_hi_alarm_limit_header, **self.roc_alarm_limit_header,
                                  **self.dead_band_header,
                                  **self.alarm_priority_header, **self.enable_output_header,
                                  **self.security_area_1_header, **self.security_area_2_header,
                                  **self.security_area_3_header, **self.alarm_area_1_header,
                                  **self.alarm_area_2_header,
                                  **self.alarm_area_3_header, **self.alarm_area_4_header, **self.alarm_area_5_header,
                                  **self.alarm_area_6_header, **self.alarm_area_7_header,
                                  **self.alarm_area_8_header, **self.alarm_area_9_header,
                                  **self.alarm_area_10_header,
                                  **self.alarm_area_11_header, **self.alarm_area_12_header,
                                  **self.alarm_area_13_header, **self.alarm_area_14_header,
                                  **self.alarm_area_15_header,
                                  **self.user_field_1_header, **self.user_field_2_header,
                                  **self.esig_type_header, **self.esig_allow_cont_use_header,
                                  **self.esig_xmpt_alarm_ack_header, **self.esig_unsigned_writes_header,
                                  **self.pdr_update_rate_header,
                                  **self.pdr_access_time_header, **self.pdr_deadband_header, **self.pdr_latch_header,
                                  **self.pdr_disable_output_header, **self.pdr_array_length_header,
                                  **self.hist_description_header, **self.hist_collect_header,
                                  **self.hist_interval_header,
                                  **self.hist_offset_header, **self.hist_time_res_header,
                                  **self.hist_compress_header, **self.hist_deadband_header,
                                  **self.hist_comp_type_header,
                                  **self.hist_comp_time_header, **self.scale_enabled_header,
                                  **self.scale_clamping_header, **self.scale_use_egu_header,
                                  **self.scale_raw_low_header,
                                  **self.scale_raw_high_header, **self.scale_low_header, **self.scale_high_header,
                                  }


class DI(FeedBackSignal, SingleBitSignals):
    def __init__(self, **kwargs):
        """ This is  DI type signal  -  individual  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- DI Individual Attributes ------------------------------------ #
        self.block_type = kwargs.get("block_type", "DI")
        self.alarm_type = kwargs.get("alarm_type", "CLOSE")
        self.event_messages = kwargs.get("event_messages", "DISABLE")
        # -------------------------------- DI Individual Headers ------------------------------------ #
        self.hist_comp_time_header = kwargs.get("hist_comp_time_header", {"Hist Comp Time]": "A_HIST_COMPTIME!"})
        self.alarm_type_header = kwargs.get("alarm_type_header", {"ALARM TYPE": "A_ALMCK"})
        self.event_messages_header = kwargs.get("event_messages_header", {"EVENT MESSAGES": "A_EVENT"})
        # -------------------------------- DI List  ------------------------------------ #
        self.attributes = di_col_list(self)
        # -------------------------------- DI Dictionary ------------------------------------ #
        self.header_attributes = {**self.block_type_header, **self.tag_header, **self.next_block_header,
                                  **self.description_header, **self.i_o_device_header, **self.h_w_options_header,
                                  **self.i_o_address_header, **self.initial_a_m_status_header,
                                  **self.initial_scan_header,
                                  **self.scan_time_header, **self.invert_output_header, **self.open_tag_header,
                                  **self.close_tag_header, **self.alarm_enable_header, **self.alarm_area_s_header,
                                  **self.alarm_priority_header, **self.alarm_type_header,
                                  **self.event_messages_header,
                                  **self.security_area_1_header, **self.security_area_2_header,
                                  **self.security_area_3_header, **self.enable_output_header,
                                  **self.alarm_area_1_header,
                                  **self.alarm_area_2_header, **self.alarm_area_3_header, **self.alarm_area_4_header,
                                  **self.alarm_area_5_header, **self.alarm_area_6_header, **self.alarm_area_7_header,
                                  **self.alarm_area_8_header, **self.alarm_area_9_header,
                                  **self.alarm_area_10_header,
                                  **self.alarm_area_11_header, **self.alarm_area_12_header,
                                  **self.alarm_area_13_header,
                                  **self.alarm_area_14_header, **self.alarm_area_15_header,
                                  **self.user_field_1_header,
                                  **self.user_field_2_header, **self.esig_type_header,
                                  **self.esig_allow_cont_use_header,
                                  **self.esig_xmpt_alarm_ack_header, **self.esig_unsigned_writes_header,
                                  **self.pdr_update_rate_header, **self.pdr_access_time_header,
                                  **self.pdr_deadband_header,
                                  **self.pdr_latch_header, **self.pdr_disable_output_header,
                                  **self.pdr_array_length_header,
                                  **self.hist_description_header, **self.hist_collect_header,
                                  **self.hist_interval_header,
                                  **self.hist_offset_header, **self.hist_time_res_header,
                                  **self.hist_compress_header,
                                  **self.hist_deadband_header, **self.hist_comp_type_header,
                                  **self.hist_comp_time_header,
                                  }


class AR(ScalableSignal):
    def __init__(self, **kwargs):
        """ This is  AR type signal  -  individual  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- AR Individual Attributes ------------------------------------ #
        self.block_type = kwargs.get("block_type", "AR")
        self.i_o_address_type = kwargs.get("i_o_address_type", "DECIMAL")
        self.event_messages = kwargs.get("event_messages", "DISABLE")
        # -------------------------------- AR Individual Headers ------------------------------------ #
        self.i_o_address_type_header = kwargs.get("i_o_address_type_header", {"I/O ADDRESS TYPE": "A_NUMS"})
        self.event_messages_header = kwargs.get("event_messages_header", {"EVENT MESSAGES": "A_EVENT"})
        # -------------------------------- AR List  ------------------------------------ #
        self.attributes = ar_col_list(self)
        # -------------------------------- AR Dictionary ------------------------------------ #
        self.header_attributes = {**self.block_type_header, **self.tag_header, **self.description_header,
                                  **self.i_o_device_header, **self.h_w_options_header,
                                  **self.i_o_address_type_header, **self.i_o_address_header,
                                  **self.signal_conditioning_header, **self.low_egu_limit_header,
                                  **self.high_egu_limit_header, **self.egu_tag_header, **self.enable_output_header,
                                  **self.event_messages_header, **self.security_area_1_header,
                                  **self.security_area_2_header, **self.security_area_3_header,
                                  **self.user_field_1_header, **self.user_field_2_header, **self.esig_type_header,
                                  **self.esig_allow_cont_use_header, **self.esig_xmpt_alarm_ack_header,
                                  **self.esig_unsigned_writes_header, **self.pdr_update_rate_header,
                                  **self.pdr_access_time_header, **self.pdr_deadband_header, **self.pdr_latch_header,
                                  **self.pdr_disable_output_header, **self.pdr_array_length_header,
                                  **self.hist_description_header, **self.hist_collect_header,
                                  **self.hist_interval_header, **self.hist_offset_header,
                                  **self.hist_time_res_header, **self.hist_compress_header,
                                  **self.hist_deadband_header, **self.hist_comp_type_header,
                                  **self.hist_comp_time_header, **self.scale_enabled_header,
                                  **self.scale_clamping_header, **self.scale_use_egu_header,
                                  **self.scale_raw_low_header, **self.scale_raw_high_header, **self.scale_low_header,
                                  **self.scale_high_header,
                                  }


class DR(SingleBitSignals):
    def __init__(self, **kwargs):
        """ This is  DR type signal  -  individual  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- DR Individual Attributes ------------------------------------ #
        self.block_type = kwargs.get("block_type", "DR")
        self.i_o_address_type = kwargs.get("i_o_address_type", "DECIMAL")
        self.event_messages = kwargs.get("event_messages", "DISABLE")
        # -------------------------------- DR Individual Headers ------------------------------------ #
        self.i_o_address_type_header = kwargs.get("i_o_address_type_header", {"I/O ADDRESS TYPE": "A_NUMS"})
        self.event_messages_header = kwargs.get("event_messages_header", {"EVENT MESSAGES": "A_EVENT"})
        self.hist_comp_time_header = kwargs.get("hist_comp_time_header", {"Hist Comp Time]": "A_HIST_COMPTIME!"})
        # -------------------------------- DR List  ------------------------------------ #
        self.attributes = dr_col_list(self)
        # -------------------------------- DR Dictionary ------------------------------------ #
        self.header_attributes = {**self.block_type_header, **self.tag_header, **self.description_header,
                                  **self.i_o_device_header, **self.h_w_options_header,
                                  **self.i_o_address_type_header, **self.i_o_address_header,
                                  **self.enable_output_header, **self.invert_output_header, **self.open_tag_header,
                                  **self.close_tag_header, **self.event_messages_header,
                                  **self.security_area_1_header, **self.security_area_2_header,
                                  **self.security_area_3_header, **self.user_field_1_header,
                                  **self.user_field_2_header, **self.esig_type_header,
                                  **self.esig_allow_cont_use_header, **self.esig_xmpt_alarm_ack_header,
                                  **self.esig_unsigned_writes_header, **self.pdr_update_rate_header,
                                  **self.pdr_access_time_header, **self.pdr_deadband_header, **self.pdr_latch_header,
                                  **self.pdr_disable_output_header, **self.pdr_array_length_header,
                                  **self.hist_description_header, **self.hist_collect_header,
                                  **self.hist_interval_header, **self.hist_offset_header,
                                  **self.hist_time_res_header, **self.hist_compress_header,
                                  **self.hist_deadband_header, **self.hist_comp_type_header,
                                  **self.hist_comp_time_header,
                                  }


class DA(FeedBackSignal, SingleBitSignals):
    def __init__(self, **kwargs):
        """ This is  DA type signal  -  individual  characteristics """
        super().__init__(**kwargs)
        # -------------------------------- DA Individual Attributes ------------------------------------ #
        self.block_type = kwargs.get("block_type", "DA")
        self.alarm_type = kwargs.get("alarm_type", "CLOSE")
        self.event_messages = kwargs.get("event_messages", "DISABLE")
        self.contact_tag = kwargs.get("contact_tag", "")
        self.contact_mode = kwargs.get("contact_mode", "")
        self.remote_ack_tag = kwargs.get("remote_ack_tag", "")
        self.alarm_suspension_tag = kwargs.get("alarm_suspension_tag", "")
        self.delay_time = kwargs.get("delay_time", "0:00:00")
        self.realarm_time = kwargs.get("realarm_time", "0:00:00")
        self.continuous_contact_output = kwargs.get("continuous_contact_output", "DISABLE")
        self.suppress_comm_alarm = kwargs.get("suppress_comm_alarm", "DISABLE")
        # -------------------------------- DA Individual Headers ------------------------------------ #
        self.alarm_type_header = kwargs.get("alarm_type_header", {"ALARM TYPE": "A_ALMCK"})
        self.contact_tag_header = kwargs.get("contact_tag_header", {"CONTACT TAG": "A_CCALM"})
        self.contact_mode_header = kwargs.get("contact_mode_header", {"CONTACT MODE": "A_CCMOD"})
        self.remote_ack_tag_header = kwargs.get("remote_ack_tag_header", {"REMOTE ACK TAG": "A_AACK"})
        self.alarm_suspension_tag_header = kwargs.get("alarm_suspension_tag_header",
                                                      {"ALARM SUSPENSION TAG": "A_ASUSP"})
        self.delay_time_header = kwargs.get("delay_time_header", {"DELAY TIME": "A_DELAY"})
        self.realarm_time_header = kwargs.get("realarm_time_header", {"REALARM TIME": "A_REALM"})
        self.continuous_contact_output_header = kwargs.get("continuous_contact_output_header",
                                                           {"Continuous Contact Output": "A_CTK_PERSIST"})
        self.suppress_comm_alarm_header = kwargs.get("suppress_comm_alarm_header",
                                                     {"Suppress COMM Alarm]": "A_COMM_SURPRESS!"})
        # -------------------------------- DA List  ------------------------------------ #
        self.attributes = da_col_list(self)
        # -------------------------------- DA Dictionary ------------------------------------ #
        self.header_attributes = {**self.block_type_header, **self.tag_header, **self.next_block_header,
                                  **self.description_header, **self.i_o_device_header, **self.h_w_options_header,
                                  **self.i_o_address_header, **self.initial_a_m_status_header,
                                  **self.initial_scan_header,
                                  **self.scan_time_header, **self.invert_output_header, **self.open_tag_header,
                                  **self.close_tag_header, **self.alarm_enable_header, **self.alarm_area_s_header,
                                  **self.alarm_priority_header, **self.alarm_type_header, **self.alarm_type_header,
                                  **self.enable_output_header, **self.security_area_1_header,
                                  **self.security_area_2_header,
                                  **self.security_area_3_header, **self.alarm_area_1_header,
                                  **self.alarm_area_2_header, **self.alarm_area_3_header, **self.alarm_area_4_header,
                                  **self.alarm_area_5_header, **self.alarm_area_6_header, **self.alarm_area_7_header,
                                  **self.alarm_area_8_header, **self.alarm_area_9_header,
                                  **self.alarm_area_10_header,
                                  **self.alarm_area_11_header, **self.alarm_area_12_header,
                                  **self.alarm_area_13_header,
                                  **self.alarm_area_14_header, **self.alarm_area_15_header,
                                  **self.user_field_1_header,
                                  **self.user_field_2_header, **self.contact_tag_header, **self.contact_mode_header,
                                  **self.remote_ack_tag_header, **self.alarm_suspension_tag_header,
                                  **self.delay_time_header, **self.realarm_time_header, **self.esig_type_header,
                                  **self.esig_allow_cont_use_header,
                                  **self.esig_xmpt_alarm_ack_header, **self.esig_unsigned_writes_header,
                                  **self.pdr_update_rate_header, **self.pdr_access_time_header,
                                  **self.pdr_deadband_header,
                                  **self.pdr_latch_header, **self.pdr_disable_output_header,
                                  **self.pdr_array_length_header,
                                  **self.hist_description_header, **self.hist_collect_header,
                                  **self.hist_interval_header,
                                  **self.hist_offset_header, **self.hist_time_res_header,
                                  **self.hist_compress_header,
                                  **self.hist_deadband_header, **self.hist_comp_type_header,
                                  **self.hist_comp_time_header,
                                  **self.continuous_contact_output_header, **self.suppress_comm_alarm_header,
                                  }


def ai_col_list(item) -> list:
    """Return/Refresh the attributes of the AI Row """
    return [item.block_type, item.tag, item.next_block, item.description, item.initial_scan,
            item.scan_time, item.smoothing, item.i_o_device, item.h_w_options,
            item.i_o_address, item.signal_conditioning, item.low_egu_limit, item.high_egu_limit,
            item.egu_tag, item.initial_a_m_status, item.alarm_enable, item.alarm_area_s,
            item.lo_lo_alarm_limit, item.lo_alarm_limit, item.hi_alarm_limit,
            item.hi_hi_alarm_limit, item.roc_alarm_limit, item.dead_band, item.alarm_priority,
            item.enable_output, item.security_area_1, item.security_area_2, item.security_area_3,
            item.alarm_area_1, item.alarm_area_2, item.alarm_area_3, item.alarm_area_4,
            item.alarm_area_5, item.alarm_area_6, item.alarm_area_7, item.alarm_area_8,
            item.alarm_area_9, item.alarm_area_10, item.alarm_area_11, item.alarm_area_12,
            item.alarm_area_13, item.alarm_area_14, item.alarm_area_15, item.user_field_1,
            item.user_field_2, item.esig_type, item.esig_allow_cont_use, item.esig_xmpt_alarm_ack,
            item.esig_unsigned_writes, item.pdr_update_rate, item.pdr_access_time, item.pdr_deadband,
            item.pdr_latch, item.pdr_disable_output, item.pdr_array_length, item.hist_description,
            item.hist_collect, item.hist_interval, item.hist_offset, item.hist_time_res,
            item.hist_compress, item.hist_deadband, item.hist_comp_type, item.hist_comp_time,
            item.scale_enabled, item.scale_clamping, item.scale_use_egu, item.scale_raw_low,
            item.scale_raw_high, item.scale_low, item.scale_high,
            ]


def di_col_list(item) -> list:
    """Return/Refresh the attributes of the DI Row """
    return [item.block_type, item.tag, item.next_block, item.description, item.i_o_device,
            item.h_w_options, item.i_o_address, item.initial_a_m_status, item.initial_scan,
            item.scan_time, item.invert_output, item.open_tag, item.close_tag, item.alarm_enable,
            item.alarm_area_s, item.alarm_priority, item.alarm_type, item.event_messages,
            item.security_area_1, item.security_area_2, item.security_area_3, item.enable_output,
            item.alarm_area_1, item.alarm_area_2, item.alarm_area_3, item.alarm_area_4,
            item.alarm_area_5, item.alarm_area_6, item.alarm_area_7, item.alarm_area_8,
            item.alarm_area_9, item.alarm_area_10, item.alarm_area_11, item.alarm_area_12,
            item.alarm_area_13, item.alarm_area_14, item.alarm_area_15, item.user_field_1,
            item.user_field_2, item.esig_type, item.esig_allow_cont_use, item.esig_xmpt_alarm_ack,
            item.esig_unsigned_writes, item.pdr_update_rate, item.pdr_access_time, item.pdr_deadband,
            item.pdr_latch, item.pdr_disable_output, item.pdr_array_length, item.hist_description,
            item.hist_collect, item.hist_interval, item.hist_offset, item.hist_time_res,
            item.hist_compress, item.hist_deadband, item.hist_comp_type, item.hist_comp_time,
            ]


def ar_col_list(item) -> list:
    """Return/Refresh the attributes of the AR Row """
    return [item.block_type, item.tag, item.description, item.i_o_device, item.h_w_options,
            item.i_o_address_type, item.i_o_address, item.signal_conditioning, item.low_egu_limit,
            item.high_egu_limit, item.egu_tag, item.enable_output, item.event_messages,
            item.security_area_1, item.security_area_2, item.security_area_3, item.user_field_1,
            item.user_field_2, item.esig_type, item.esig_allow_cont_use, item.esig_xmpt_alarm_ack,
            item.esig_unsigned_writes, item.pdr_update_rate, item.pdr_access_time, item.pdr_deadband,
            item.pdr_latch, item.pdr_disable_output, item.pdr_array_length, item.hist_description,
            item.hist_collect, item.hist_interval, item.hist_offset, item.hist_time_res,
            item.hist_compress, item.hist_deadband, item.hist_comp_type, item.hist_comp_time,
            item.scale_enabled, item.scale_clamping, item.scale_use_egu, item.scale_raw_low,
            item.scale_raw_high, item.scale_low, item.scale_high,
            ]


def dr_col_list(item) -> list:
    """Return/Refresh the attributes of the DR Row """
    return [item.block_type, item.tag, item.description, item.i_o_device, item.h_w_options,
            item.i_o_address_type, item.i_o_address, item.enable_output, item.invert_output,
            item.open_tag, item.close_tag, item.event_messages, item.security_area_1,
            item.security_area_2, item.security_area_3, item.user_field_1, item.user_field_2,
            item.esig_type, item.esig_allow_cont_use, item.esig_xmpt_alarm_ack,
            item.esig_unsigned_writes, item.pdr_update_rate, item.pdr_access_time, item.pdr_deadband,
            item.pdr_latch, item.pdr_disable_output, item.pdr_array_length, item.hist_description,
            item.hist_collect, item.hist_interval, item.hist_offset, item.hist_time_res,
            item.hist_compress, item.hist_deadband, item.hist_comp_type, item.hist_comp_time,
            ]


def da_col_list(item) -> list:
    """Return/Refresh the attributes of the DA Row """
    return [item.block_type, item.tag, item.next_block, item.description, item.i_o_device,
            item.h_w_options, item.i_o_address, item.initial_a_m_status, item.initial_scan,
            item.scan_time, item.invert_output, item.open_tag, item.close_tag, item.alarm_enable,
            item.alarm_area_s, item.alarm_priority, item.alarm_type, item.enable_output,
            item.security_area_1, item.security_area_2, item.security_area_3,
            item.alarm_area_1, item.alarm_area_2, item.alarm_area_3, item.alarm_area_4,
            item.alarm_area_5, item.alarm_area_6, item.alarm_area_7, item.alarm_area_8,
            item.alarm_area_9, item.alarm_area_10, item.alarm_area_11, item.alarm_area_12,
            item.alarm_area_13, item.alarm_area_14, item.alarm_area_15, item.user_field_1,
            item.user_field_2, item.contact_tag, item.contact_mode, item.remote_ack_tag,
            item.alarm_suspension_tag, item.delay_time, item.realarm_time,
            item.esig_type, item.esig_allow_cont_use, item.esig_xmpt_alarm_ack,
            item.esig_unsigned_writes, item.pdr_update_rate, item.pdr_access_time, item.pdr_deadband,
            item.pdr_latch, item.pdr_disable_output, item.pdr_array_length, item.hist_description,
            item.hist_collect, item.hist_interval, item.hist_offset, item.hist_time_res,
            item.hist_compress, item.hist_deadband, item.hist_comp_type, item.hist_comp_time,
            item.continuous_contact_output, item.suppress_comm_alarm,
            ]
