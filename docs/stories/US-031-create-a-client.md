# US-031 · Create a client

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E3 · Clients | Must | P1 | M | To do |

- **Depends on:** [US-030](US-030-find-and-select-a-client.md)
- **Decisions:** [ADR-0011](../adr/0011-localisation.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-03, R-04 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to create a client with the information the contract needs, so that their details are printed correctly and reused next time.

## Acceptance criteria

- [ ] Fields from the current contract:
  - full name;
  - home/billing address: street, second line, postcode, city, country (the country is added, default for R-03);
  - phone;
  - local address and its phone;
  - licence number;
  - date of birth, and place or country of birth;
  - ID document type (passport or ID card), number and country.
- [ ] Only the full name is needed to save the record. Before a Départ can be signed, these are mandatory (default for R-03): full name, home address, licence number, date of birth, ID document number. These are the fields filled on the completed sample.
- [ ] Field lengths follow the limits set in US-006.
- [ ] The date of birth can't be in the future. The age is displayed, with no warning or blocking (default for R-04).
- [ ] Possible duplicates are flagged before saving: the same name and date of birth, or the same licence or ID number.
- [ ] The creation is recorded in the audit trail.

## Notes

- What the country written after the date of birth and after the ID number means is still open (R-03 Q3). The field labels stay neutral until it's answered.
