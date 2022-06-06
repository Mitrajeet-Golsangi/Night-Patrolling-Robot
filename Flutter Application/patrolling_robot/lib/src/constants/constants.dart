class Constants {
  static String videoWebsocketURL = "ws://192.168.29.196:5000";

  static void setVideoWebsocketURL(String host, String port) =>
      Constants.videoWebsocketURL = "ws://" + host + ":" + port;
}
