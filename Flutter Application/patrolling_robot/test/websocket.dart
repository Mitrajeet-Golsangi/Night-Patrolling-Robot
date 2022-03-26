import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:web_socket_channel/status.dart' as status;

void main() async {
  const url = "ws://192.168.29.155:5000";

  final WebSocketChannel channel = IOWebSocketChannel.connect(Uri.parse(url));

  channel.stream.listen((msg) {
    print(msg);
    print(msg.runtimeType);

    channel.sink.add('Received');
    channel.sink.close(status.goingAway);
  });
}
