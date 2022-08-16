#!/usr/bin/node
if (process.argv.length > 3) {
  // TODO: Turn the argument into a array (slice) and convert the element into integers with (map)
  const args = process.argv.slice(2, process.argv.length).map(Number);
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
