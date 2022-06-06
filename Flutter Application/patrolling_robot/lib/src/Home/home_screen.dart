import 'package:flutter/material.dart';
import 'package:patrolling_robot/src/Network/network.dart';
import 'package:patrolling_robot/src/VideoStream/VideoStreaming.dart';
import 'package:patrolling_robot/src/styles/styles.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Home"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Center(
          child: Column(
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  ElevatedButton(
                    onPressed: () =>
                        {Navigator.pushNamed(context, Network.route)},
                    style: Styles.buttonStyle2,
                    child: const Text("Connect With Robot"),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  ElevatedButton(
                    onPressed: () =>
                        {Navigator.pushNamed(context, VideoStream.route)},
                    style: Styles.buttonStyle2,
                    child: const Text("Start Live Stream"),
                  ),
                ],
              ),
              const SizedBox(
                height: 50.0,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
