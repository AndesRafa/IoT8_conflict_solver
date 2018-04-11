DROP TABLE IF EXISTS Conflict;
CREATE TABLE Conflict (
    ID INTEGER PRIMARY KEY,
    ApiName VARCHAR(500),
    OldApiVersion VARCHAR(50),
    NewApiVersion VARCHAR(50),
    Path VARCHAR(500),
    OldValue VARCHAR(500),
    NewValue VARCHAR(500)
);

DROP TABLE IF EXISTS Taxonomy;
CREATE TABLE Taxonomy (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    Description VARCHAR(500),
    Solution VARCHAR(500)
);

DROP TABLE IF EXISTS Resolution;
CREATE TABLE Resolution (
    ID INTEGER PRIMARY KEY,
    ConflictID INTEGER,
    TaxonomyID INTEGER,
    NodeChain VARCHAR(500),

    FOREIGN KEY (ConflictID) REFERENCES Conflict(ID),
    FOREIGN KEY (TaxonomyID) REFERENCES Taxonomy(ID)
);
