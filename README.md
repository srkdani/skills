# skills

Agent skills for design and building with AI.

Each skill packages one expert's judgment as concrete, checkable rules, so an agent can act on vague requests like "make it better" with specific decisions instead of defaults.

## Skills

| Skill | Use it when |
|---|---|
| [ai-ui-tells](ai-ui-tells/SKILL.md) | Building, reviewing, or polishing any UI, especially when asked to make it "better" or "less AI", or when it "looks generic" or "looks AI-made". Commits to a named art direction, then replaces generated-UI defaults, including the looks people adopt to escape those defaults. Includes a self-audit and an [eval](ai-ui-tells/eval/README.md). |

## Install

A skill is a folder with a `SKILL.md` file. Copy the folder into your project's agent skills directory:

```sh
git clone https://github.com/srkdani/skills
mkdir -p your-project/.agents/skills
cp -r skills/ai-ui-tells your-project/.agents/skills/
```

If your agent reads skills from a different folder (for example a user-level skills directory in your home folder), copy `ai-ui-tells/` there instead. The agent picks the skill up from the `description` in its frontmatter, so no other setup is needed. You can also point the agent at the file directly: "Use .agents/skills/ai-ui-tells/SKILL.md".

## License

MIT
