class CounterState {
  final int count;

  CounterState({required this.count});

  factory CounterState.initial() => CounterState(count: 0);
}
