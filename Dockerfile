FROM alpine:latest
WORKDIR ./
COPY helloUser.cpp ./ .
SHELL ["zsh", "bash"]
CMD ["g++", "-std=c++0x", "helloUser.cpp -o helloUser"]

