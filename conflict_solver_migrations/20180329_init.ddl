CREATE TABLE Conflict (
    ID INTEGER PRIMARY KEY,
    ApiName VARCHAR(500),
    ApiVersion VARCHAR(50),
    Path VARCHAR(500),
    Value VARCHAR(500)
);

CREATE TABLE Taxonomy (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    Description VARCHAR(500),
    Solution VARCHAR(500)
);

CREATE TABLE Resolution (
    ID INTEGER PRIMARY KEY,
    ConflictID INTEGER,
    TaxonomyID INTEGER,
    NodeChain VARCHAR(500),

    FOREIGN KEY (ConflictID) REFERENCES Conflict(ID),
    FOREIGN KEY (TaxonomyID) REFERENCES Taxonomy(ID)
);
