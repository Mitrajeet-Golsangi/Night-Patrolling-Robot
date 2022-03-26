import 'package:flutter_bloc';
import 'package:meta/meta.dart';

part 'videostream_event.dart';
part 'videostream_state.dart';

class VideostreamBloc extends Bloc<VideostreamEvent, VideostreamState> {
  VideostreamBloc() : super(VideostreamInitial()) {
    on<VideostreamEvent>((event, emit) {
      // TODO: implement event handler
    });
  }
}
