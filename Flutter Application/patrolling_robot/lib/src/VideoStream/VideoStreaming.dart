import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:patrolling_robot/src/VideoStream/websocket.dart';
import 'package:patrolling_robot/src/constants/constants.dart';
import 'package:patrolling_robot/src/styles/styles.dart';

class VideoStream extends StatefulWidget {
  const VideoStream({Key? key}) : super(key: key);

  @override
  State<VideoStream> createState() => _VideoStreamState();
}

class _VideoStreamState extends State<VideoStream> {
  final WebSocket _socket = WebSocket(videoWebsocketURL);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Live Video"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Center(
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  ElevatedButton(
                    onPressed: _socket.connect,
                    style: buttonStyle,
                    child: const Text("Connect"),
                  ),
                  ElevatedButton(
                    onPressed: _socket.disconnect,
                    style: buttonStyle,
                    child: const Text("Disconnect"),
                  ),
                ],
              ),
              const SizedBox(
                height: 50.0,
              ),
              _socket.connectionState
                  ? StreamBuilder(
                      stream: _socket.stream,
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
                    )
                  : const Text("Initiate Connection")
              // Image.network("ws://192.168.29.155:5000")
            ],
          ),
        ),
      ),
    );
  }
}
