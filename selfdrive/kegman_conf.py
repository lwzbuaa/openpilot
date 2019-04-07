import json
import os

class kegman_conf():
  def __init__(self, CP=None):
    self.conf = self.read_config()
    if CP is not None:
      self.init_config(CP)

  def init_config(self, CP):
    write_conf = False
    if self.conf['tuneGernby'] == "-1":
      self.conf['tuneGernby'] = str(1)
      write_conf = True
    if self.conf['rateFF'] == "-1":
      self.conf['rateFF'] = "0.2"
      write_conf = True
    if self.conf['angleFF'] == "-1":
      self.conf['angleFF'] = "2.0"
      write_conf = True
    if self.conf['reactMPC'] == "-1":
      self.conf['reactMPC'] = str(round(CP.steerMPCReactTime,3))
      write_conf = True
    if self.conf['dampMPC'] == "-1":
      self.conf['dampMPC'] = str(round(CP.steerMPCDampTime,3))
      write_conf = True
    if self.conf['leadDistance'] == "-1":
      self.conf['leadDistance'] = "45.0"
    if self.conf['Kp'] == "-1":
      self.conf['Kp'] = str(round(CP.steerKpV[0],3))
      write_conf = True
    if self.conf['Ki'] == "-1":
      self.conf['Ki'] = str(round(CP.steerKiV[0],3))
      write_conf = True

    if write_conf:
      self.write_config(self.config)

  def read_config(self):
    self.element_updated = False

    if os.path.isfile('/data/kegman.json'):
      with open('/data/kegman.json', 'r') as f:
        self.config = json.load(f)

      if "battPercOff" not in self.config:
        self.config.update({"battPercOff":"25"})
        self.config.update({"carVoltageMinEonShutdown":"11800"})
        self.config.update({"brakeStoppingTarget":"0.25"})
        self.element_updated = True

      if "tuneGernby" not in self.config:
        self.config.update({"tuneGernby":"0"})
        self.config.update({"react":"-1"})
        self.config.update({"Kp":"-1"})
        self.config.update({"Ki":"-1"})
        self.element_updated = True

      if "rateFF" not in self.config:
        self.config.update({"rateFF":"0.2"})
        self.config.update({"angleFF":"2.0"})
        self.element_updated = True

      if "dampMPC" not in self.config:
        self.config.update({"dampMPC":"-1"})
        self.config.update({"dampSteer":"-1"})
        self.element_updated = True

      if "reactMPC" not in self.config:
        self.config.update({"reactMPC":"-1"})
        self.config.update({"reactSteer":"-1"})
        self.element_updated = True

      if "leadDistance" not in self.config:
        self.config.update({"leadDistance":"45.0"})
        self.element_updated = True

      # Force update battery charge limits to higher values for Big Model
      #if self.config['battChargeMin'] != "75":
      #  self.config.update({"battChargeMin":"75"})
      #  self.config.update({"battChargeMax":"80"})
      #  self.element_updated = True

      if self.element_updated:
        self.write_config(self.config)

    else:
      self.config = {"cameraOffset":"0.06", "lastTrMode":"1", "battChargeMin":"60", "battChargeMax":"70", \
                     "wheelTouchSeconds":"86400", "battPercOff":"25", "carVoltageMinEonShutdown":"11800", \
                     "brakeStoppingTarget":"0.25", "tuneGernby":"0", "reactSteer":"-1", "reactMPC":"-1", \
                     "dampMPC":"-1", "dampSteer":"-1", "rateFF":"0.2", "angleFF":"2.0", "Kp":"-1", "Ki":"-1", "leadDistance":"45.0"}

      self.write_config(self.config)
    return self.config

  def write_config(self, config):
    with open('/data/kegman.json', 'w') as f:
      json.dump(self.config, f, indent=2, sort_keys=True)
      os.chmod("/data/kegman.json", 0o764)
