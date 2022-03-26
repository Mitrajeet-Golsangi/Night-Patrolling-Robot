import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

import 'package:web_socket_channel/status.dart' as status;

class MainPage extends StatefulWidget {
  const MainPage({Key? key}) : super(key: key);

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  static const String url = "ws://192.168.29.155:5000";
  WebSocketChannel _channel = IOWebSocketChannel.connect(Uri.parse(url));

  void connect() {
    _channel = IOWebSocketChannel.connect(Uri.parse(url));
    setState(() {});
  }

  void disconnect() {
    _channel.sink.close(status.goingAway);
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      darkTheme: ThemeData(brightness: Brightness.dark),
      themeMode: ThemeMode.dark,
      home: Scaffold(
        appBar: AppBar(
          title: const Text("Live Video"),
        ),
        body: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Center(
            child: Column(
              children: [
                Row(
                  children: [
                    ElevatedButton(
                        onPressed: connect, child: const Text("Connect")),
                    const SizedBox(
                      width: 90.0,
                    ),
                    ElevatedButton(
                        onPressed: disconnect, child: const Text("Disconnect")),
                  ],
                ),
                const SizedBox(
                  height: 50.0,
                ),
                StreamBuilder(
                  stream: _channel.stream,
                  builder: (context, snapshot) {
                    if (!snapshot.hasData) {
                      return const CircularProgressIndicator();
                    }

                    if (snapshot.connectionState == ConnectionState.done) {
                      return const Center(
                        child: Text("Connection Closed !"),
                      );
                    }
                    //? Working for single frames
                    return Image.memory(
                      Uint8List.fromList(
                        base64Decode(
                          (snapshot.data.toString()),
                        ),
                      ),
                      gaplessPlayback: true,
                    );
                  },
                ),
                // Image.network("ws://192.168.29.155:5000")
              ],
            ),
          ),
        ),
      ),
    );
  }
}
