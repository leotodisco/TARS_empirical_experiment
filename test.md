```mermaid
graph TD
    A([__start__]) --> B[plannerNode]
    B --> C[syntaxCheck]
    C -.-> B
    C -.-> D[critiqueNode]
    C -.-> E([__end__])
    D -.-> B
    D -.-> E
```
