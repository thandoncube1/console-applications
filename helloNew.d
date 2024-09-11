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
    dchar[] simpleVar;
    write("Hi, what is your name?\nName: ");
    readln(name);
    // simpleVar = name.dup; // Create a copy
    writeln("Hello ", name);
    dchar[] mixedResult = mix(name.dup, simpleVar); // store the result
    writeln("Mixed: ", mixedResult); // Print the mixed result

    return 0;
}