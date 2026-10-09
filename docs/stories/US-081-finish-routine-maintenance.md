# US-081 · Finish a routine maintenance

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E8 · Maintenance | Must | P5 | S | To do |

- **Depends on:** [US-080](US-080-put-a-vehicle-into-maintenance.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to finish routine maintenance and put the car back in service without retaking photos, so that ordinary servicing stays quick.

## Acceptance criteria

- [ ] « Terminer la maintenance » records the end date, with an optional note and odometer reading.
- [ ] For any kind other than a damage repair, no new reference photos are required (« Reset status ou pas »). Staff can still take a new set.
- [ ] The vehicle returns to `available`.
