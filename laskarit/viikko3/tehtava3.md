```mermaid
sequenceDiagram
    participant main
    participant olio
    participant Engine
    participant FuelTank
    
    main->>olio: Machine()
    olio->>FuelTank: FuelTank() 
    main->>olio: drive()
```