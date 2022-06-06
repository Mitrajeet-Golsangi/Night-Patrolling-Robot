import 'package:flutter/material.dart';
import 'package:patrolling_robot/src/Network/network_form.dart';
import 'package:patrolling_robot/src/constants/constants.dart';
import 'package:patrolling_robot/src/styles/styles.dart';

class Network extends StatefulWidget {
  const Network({Key? key}) : super(key: key);
  static const route = '/network';
  @override
  State<Network> createState() => _NetworkState();
}

class _NetworkState extends State<Network> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Network Config"),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(10.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text("Active Network", style: Styles.textStyle),
              const SizedBox(
                height: 20,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text("Current Network"),
                  Text(Constants.videoWebsocketURL.substring(5)),
                ],
              ),
              const SizedBox(
                height: 20,
              ),
              const Text("Change Network", style: Styles.textStyle),
              const SizedBox(
                height: 20,
              ),
              const NetworkForm(),
              const SizedBox(
                height: 20,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
