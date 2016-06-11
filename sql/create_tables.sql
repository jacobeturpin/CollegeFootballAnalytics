CREATE TABLE Team (
	TeamId			VARCHAR(36)		NOT NULL,
	TeamName		VARCHAR(200)	NOT NULL,
	TeamLink		VARCHAR(250)	NOT NULL	
);

CREATE TABLE Player (
	PlayerId		VARCHAR(36)		NOT NULL,
	PlayerName		VARCHAR(200)	NOT NULL,
	PlayerLink		VARCHAR(250)	NOT NULL
);

CREATE TABLE Conference (
	ConferenceId	VARCHAR(36)		NOT NULL,
	ConferenceName	VARCHAR(200)	NOT NULL,
	ConferenceLink	VARCHAR(250)	NOT NULL
);

CREATE TABLE Game (
	GameId			VARCHAR(36)		NOT NULL,
	GameLink		VARCHAR(250)	NOT NULL,
	HomeTeamId		VARCHAR(36)		NOT NULL,
	HomeTeamScore	INTEGER			NOT NULL,
	AwayTeamId		VARCHAR(36)		NOT NULL,
	AwayTeamScore	INTEGER			NOT NULL
);

CREATE TABLE PassingBoxScore (
	GameId						VARCHAR(36)		NOT NULL,
	PlayerId					VARCHAR(36)		NOT NULL,
	TeamId						VARCHAR(36)		NOT NULL,
	PassCompletions				INTEGER			NOT NULL,
	PassAttempts				INTEGER			NOT NULL,
	PassCompletionPercentage	DECIMAL			NOT NULL,
	PassYards					INTEGER			NOT NULL,
	PassYardsPerAttempt			DECIMAL			NOT NULL,
	PassAdjustedYardsPerAttempt	DECIMAL			NOT NULL,
	PassTouchdowns				INTEGER			NOT NULL,
	PassInterceptions			INTEGER			NOT NULL,
	PassEfficiencyRating		DECIMAL			NOT NULL
);

CREATE TABLE RushReceiveBoxScore (
	GameId						VARCHAR(36)		NOT NULL,
	PlayerId					VARCHAR(36)		NOT NULL,
	TeamId						VARCHAR(36)		NOT NULL,
	RushAttempts				INTEGER			NULL,
	RushYards					INTEGER			NULL,
	RushYardsPerAttempt			DECIMAL			NULL,
	RushTouchdowns				INTEGER			NULL,
	Receptions					INTEGER			NULL,
	ReceiveYards				INTEGER			NULL,
	ReceiveYardsPerReception	DECIMAL			NULL,
	ReceiveTouchdowns			INTEGER			NULL
);

CREATE TABLE DefenseBoxScore (
	GameId									VARCHAR(36)		NOT NULL,
	PlayerId								VARCHAR(36)		NOT NULL,
	TeamId									VARCHAR(36)		NOT NULL,
	SoloTackles								INTEGER			NOT NULL,
	AssistedTackles							INTEGER			NOT NULL,
	TotalTackles							INTEGER			NOT NULL,
	TacklesForLoss							DECIMAL			NOT NULL,
	Sacks									DECIMAL			NOT NULL,
	Interceptions							INTEGER			NULL,
	InterceptionReturnYards					INTEGER			NULL,
	InterceptionReturnYardsPerInterception	DECIMAL			NULL,
	InterceptionReturnTouchdowns			INTEGER			NULL,
	PassesDefended							INTEGER			NULL,
	FumblesRecovered						INTEGER			NULL,
	FumbleRecoveryYards						INTEGER			NULL,
	FumbleRecoveryTouchdowns				INTEGER			NULL,
	FumblesForced							INTEGER			NULL
);

CREATE TABLE KickPuntReturnBoxScore (
	GameId						VARCHAR(36)		NOT NULL,
	PlayerId					VARCHAR(36)		NOT NULL,
	TeamId						VARCHAR(36)		NOT NULL
	-- Stats Go Here
);

CREATE TABLE KickPuntBoxScore (
	GameId						VARCHAR(36)		NOT NULL,
	PlayerId					VARCHAR(36)		NOT NULL,
	TeamId						VARCHAR(36)		NOT NULL
	-- Stats Go Here
);
