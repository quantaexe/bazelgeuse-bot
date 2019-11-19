# bazelgeuse-bot
Discord bot that plays Bazelgeuse's scream when user joins a voice channel

Current Features:
- When a user joins a voice channel, BazelgeuseBot will join that channel and execute the scream sound file
- When a user enters the command "bazelgeuse scream", BazelgeuseBot will execute the scream sound file and print a message to
whatever text channel the user is currently on
- BazelgeuseBot will react to its name being mentioned in any text channels with a text message in response. Additionally,
if the user mentions "bazelgeuse" and "nudes" somewhere in their message, BazelgeuseBot will post a picture of itself.

Issues:
- BazelgeuseBot currently will not disconnect from the voice channel after it has joined.
