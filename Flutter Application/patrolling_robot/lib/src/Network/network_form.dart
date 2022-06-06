import 'package:flutter/material.dart';
import 'package:patrolling_robot/src/constants/constants.dart';
import 'package:patrolling_robot/src/styles/styles.dart';

class NetworkForm extends StatefulWidget {
  const NetworkForm({Key? key}) : super(key: key);

  @override
  State<NetworkForm> createState() => _NetworkFormState();
}

class _NetworkFormState extends State<NetworkForm> {
  final GlobalKey _globalKey = GlobalKey<FormState>();
  final TextEditingController _hostController = TextEditingController();
  final TextEditingController _portController = TextEditingController();

  void handleSubmit() => Constants.setVideoWebsocketURL(
      _hostController.text, _portController.text);

  @override
  Widget build(BuildContext context) {
    return Form(
        key: _globalKey,
        child: Column(
          children: [
            TextFormField(
              maxLength: 15,
              controller: _hostController,
              decoration: const InputDecoration(
                label: Text("Network IP"),
                icon: Icon(Icons.wifi),
              ),
              keyboardType: TextInputType.number,
            ),
            const SizedBox(
              height: 20,
            ),
            TextFormField(
                maxLength: 4,
                controller: _portController,
                decoration: const InputDecoration(
                  label: Text("Port"),
                  icon: Icon(Icons.usb),
                ),
                keyboardType: TextInputType.number),
            const SizedBox(
              height: 20,
            ),
            ElevatedButton(
              onPressed: handleSubmit,
              child: const Text("Submit"),
              style: Styles.buttonStyle2,
            )
          ],
        ));
  }
}
