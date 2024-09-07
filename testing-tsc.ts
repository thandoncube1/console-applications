// Welcome to TypeScript
function location(name, birthPlace) {
  return {
    name,
    birthPlace,
    getName: function() {
      console.log(this.name);
      console.error("This is an error code.");
    }
  }
}

console.log(location("Thando", "Bulawayo, Zimbabwe"));
