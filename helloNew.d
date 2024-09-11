import std.stdio;

dchar[] mix(immutable dchar[] first,
            immutable dchar[] second) {
    dchar[] result;
    int i;

    for (i = 0; (i < first.length) && (i < second.length); ++i) {
        result ~= first[i];
        result ~= second[i];
    }

    result ~= first[i..$];
    result ~= second[i..$];

    return result;
}


int main() {
    char[] name;

    write("Hi, what is your name?\nName: ");
    readln(name);
    writeln("Hello ", name);

    return 0;
}