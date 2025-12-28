# Remedial Legitimacy Framework - Development Guidelines

## Instrument Development Workflow

### 1. Proposal Phase

When proposing a new instrument:
1. Create a GitHub issue using the "Instrument Proposal" template
2. Fill out all sections thoroughly:
   - Identify the gap or failure mode being addressed
   - Explain the mechanism of operation
   - Specify the instrument category
   - Define ethical constraints
   - Provide potential applications
   - Note historical/contemporary analogues
3. Engage in discussion and refinement in issue comments
4. Once concept is approved, proceed to drafting phase

### 2. Drafting Phase

When drafting an instrument:
1. Fetch latest main and create a new branch: `git checkout main && git pull && git checkout -b draft/instrument-name`
2. Create a GitHub issue using the "Draft Instrument" template (or reference existing proposal)
3. Copy `templates/INSTRUMENT_TEMPLATE.md` to `proposals/instrument-name.md`
4. Draft the instrument following the template structure:
   - **Preamble**: Contextual framing and necessity
   - **Definitions**: Clear terminology
   - **Core Mechanism**: Primary operational logic
   - **Activation Conditions**: When instrument becomes operational
   - **Documentation Requirements**: What must be recorded
   - **Authority Granted**: Specific powers/capacities established
   - **Ethical Constraints**: Self-limiting provisions
   - **Sunset Provisions**: Termination conditions
   - **Execution**: Signature/witnessing requirements
   - **Commentary**: Theoretical analysis and context

### 3. Review and Feedback Phase

Before creating a pull request:
1. **Self-review**: Ensure all template sections are complete
2. **Theoretical coherence**: Verify alignment with framework principles (see `docs/THEORETICAL_FOUNDATIONS.md`)
3. **Ethical review**: Confirm adequate protections against misuse
4. **Precedent research**: Identify legal/historical analogues
5. **External feedback** (optional): Use Perplexity API or similar to gather:
   - Legal precedent citations
   - Historical analogues
   - Theoretical critiques
   - Potential vulnerabilities

### 4. Pull Request Phase

When creating a pull request:
1. Create PR with descriptive title: `[DRAFT] Instrument Name`
2. Link to the proposal issue in PR description
3. Include in PR description:
   - Summary of instrument's purpose
   - Key innovations or mechanisms
   - Category classification
   - Any open questions or areas needing review
4. Add any external feedback as PR comments (Perplexity API analysis, legal research, etc.)
5. Request review from at least one other contributor
6. Address all review comments

### 5. Ratification Phase

Once PR is approved:
1. Move instrument from `proposals/` to `instruments/`
2. Update status in `docs/INSTRUMENT_TAXONOMY.md` from [DRAFTED] to [RATIFIED]
3. Create companion analysis document (`.md` file) if instrument is in PDF format
4. Update `instruments/README.md` with new entry
5. Update main `README.md` collection count if needed
6. Merge PR

## Using AI Feedback in Development

### Perplexity API Integration

Use the Perplexity API to enhance instrument development:

```bash
# Set API key (should be in environment)
export PERPLEXITY_API_KEY="your-key-here"
```

**Recommended queries for draft instruments**:
1. "What legal precedents exist for [mechanism description]?"
2. "Historical examples of [instrument concept] in law or social movements?"
3. "Potential legal vulnerabilities in [brief instrument description]?"
4. "Case law related to [specific provisions]?"
5. "Constitutional law scholarship on [theoretical foundation]?"

Add API responses as PR comments to document research and provide context for reviewers.

## Quality Standards

### All Instruments Must Include:
- Clear activation conditions
- Ethical constraints and self-limiting provisions
- Documentation requirements
- Sunset or transfer mechanisms
- Relationship to existing legal frameworks

### Theoretical Rigor:
- Ground in framework's theoretical foundations
- Explain gap or failure mode addressed
- Show how instrument relates to existing law
- Identify which framework category it belongs to

### Ethical Standards:
- Include prohibition on creating new harms
- Require good-faith institutional engagement
- Establish accountability mechanisms
- Provide sunset mechanisms upon remedy

## Branch Naming Convention

- Proposals: `proposal/instrument-name`
- Drafts: `draft/instrument-name`
- Documentation: `docs/topic-name`
- Fixes: `fix/issue-description`

## Commit Message Format

Use descriptive commit messages following this pattern:

```
[ACTION] Brief description

Detailed explanation of changes, including:
- What was added/modified
- Why the change was made
- Key innovations or mechanisms
- Related issues or PRs

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

## Documentation Requirements

### For Each Ratified Instrument:
1. The instrument itself (PDF or markdown)
2. Companion analysis document including:
   - Overview and summary
   - Core innovations
   - Key mechanisms
   - Theoretical significance
   - Practical applications
   - Relationship to other instruments
   - Historical analogues
   - Limitations and constraints
   - Usage guidelines
   - Open questions

### Update These Files:
- `docs/INSTRUMENT_TAXONOMY.md` - Update instrument status
- `instruments/README.md` - Add entry to collection
- `README.md` - Update collection count

## Testing and Validation

While these are theoretical documents, validate by:
1. **Theoretical consistency**: Does it align with framework principles?
2. **Internal coherence**: Are all sections logically connected?
3. **Completeness**: Are all template sections addressed?
4. **Ethical soundness**: Are protections against misuse adequate?
5. **Precedent research**: Have analogues been identified?
6. **Peer review**: Has it been reviewed by at least one other person?

## Notes

- This is a theoretical and documentary project
- Instruments are not legally enforceable documents
- Focus on theoretical rigor and ethical constraints
- Document thoroughly for future accountability and reference
- Prioritize clarity and accessibility in language while maintaining precision
