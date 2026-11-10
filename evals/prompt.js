// Builds the chat for one test case: the persona file as the system prompt,
// then the scripted turns from the case (`turns: [{user}, {assistant}, ...]`).
// The model under test answers the final user turn.
const fs = require('fs');
const path = require('path');

// Where the persona files live. Kept in one place so the layout can move.
const PERSONA_DIR = process.env.PERSONA_DIR || 'dist/prompts';

module.exports = async function ({ vars }) {
  const file = path.resolve(__dirname, '..', PERSONA_DIR, `${vars.persona}.md`);
  const messages = [{ role: 'system', content: fs.readFileSync(file, 'utf8') }];
  for (const turn of vars.turns) {
    if (turn.user !== undefined) messages.push({ role: 'user', content: turn.user });
    if (turn.assistant !== undefined) messages.push({ role: 'assistant', content: turn.assistant });
  }
  return messages;
};
