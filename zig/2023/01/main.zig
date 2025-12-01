const std = @import("std");

pub fn main() void {

    var file = try std.fs.cwd().openFile("example.txt", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();
    var buf: [10]u8 = undefined;

    var total: u16 = 0;
    while (try in_stream.readUntilDelimiterOrEof(buf[0..], '\n')) |line| {
        var result = try std.fmt.parseInt(u16, line, 10);
        _ = result;
        total += 1;
        std.debug.print("increments {d}\n", .{total});
    }
    std.debug.print("increments {d}\n", .{total});
}
