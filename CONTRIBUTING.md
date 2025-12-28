# Contributing to the Remedial Legitimacy Framework

## How to Propose a New Instrument

1. Create a new issue using the "Instrument Proposal" template
2. Fill out all sections of the template
3. Label the issue with the appropriate category (gap-bridging, distributed-accountability, etc.)
4. Engage in discussion and refinement in the issue comments

## How to Draft an Instrument

1. Create a new issue using the "Draft Instrument" template (or reference an existing proposal)
2. Create a new branch: `git checkout -b draft/instrument-name`
3. Copy `templates/INSTRUMENT_TEMPLATE.md` to `proposals/instrument-name.md`
4. Draft the instrument following the template structure
5. Create a pull request linking to the proposal issue
6. Request review and incorporate feedback
7. Once approved, the instrument moves from `proposals/` to `instruments/`

## Instrument Drafting Guidelines

### Structure
- Follow the template structure in `templates/INSTRUMENT_TEMPLATE.md`
- Use precise legal language while maintaining accessibility
- Include clear definitions for all terms of art
- Document the theoretical basis in the Commentary section

### Key Elements
Every instrument should include:
- **Clear activation conditions**: When does this instrument become operational?
- **Ethical constraints**: What prevents misuse?
- **Documentation requirements**: What must be recorded?
- **Sunset provisions**: When/how does the instrument cease operation?

### Theoretical Rigor
- Ground instruments in the theoretical foundations (see `docs/THEORETICAL_FOUNDATIONS.md`)
- Identify which category the instrument belongs to
- Explain the gap or failure mode being addressed
- Show how the instrument relates to existing legal frameworks

### Ethical Standards
All instruments must:
- Include self-limiting clauses
- Prohibit creation of new harms
- Require good-faith engagement with existing institutions
- Establish accountability mechanisms
- Provide sunset or transfer mechanisms

## Pull Request Process

1. Ensure your branch is up to date with `main`
2. Your PR description should include:
   - Link to the proposal issue
   - Summary of the instrument's purpose
   - Key innovations or mechanisms
   - Any open questions or areas needing review
3. Request review from at least one other contributor
4. Address all review comments
5. Once approved, the maintainer will merge and move to `instruments/` if ready

## Review Criteria

Reviewers should evaluate:
- **Theoretical coherence**: Does it align with framework principles?
- **Clarity**: Is the language precise and understandable?
- **Completeness**: Are all template sections adequately addressed?
- **Ethical constraints**: Are protections against misuse sufficient?
- **Novelty**: Does it add something new to the framework?
- **Practical applicability**: Could this instrument serve its stated purpose?

## Brainstorming and Discussion

- Use GitHub Discussions for general brainstorming
- Use issues for specific instrument proposals
- Tag related instruments and proposals for cross-reference
- Build on existing instruments where possible

## Code of Conduct

This is a theoretical and documentary project. All contributions should:
- Focus on addressing genuine gaps in accountability and legitimacy
- Avoid creating instruments that could facilitate harm
- Engage respectfully with existing legal frameworks
- Acknowledge limitations and constraints
- Prioritize transparency and documentation

## Questions?

Open a discussion thread or comment on relevant issues.
