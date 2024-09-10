import std.stdio;

int main() {
    char[] name;

    write("Hi, what is your name?\nName: ");
    readln(name);
    writeln("Hello ", name);

    return 0;
}