import 'package:web_socket_channel/web_socket_channel.dart';

class WebSocket {
  final channel = WebSocketChannel.connect(Uri.parse("ws://127.0.0.1:5000"));
}
