CREATE TABLE Team (
	TeamId			VARCHAR(36)		NOT NULL,
	TeamName		VARCHAR(200)	NOT NULL,
	TeamLink		VARCHAR(250)	NOT NULL	
);

CREATE TABLE Player (
	PlayerId			VARCHAR(36)		NOT NULL,
	PlayerName		VARCHAR(200)	NOT NULL,
	PlayerLink		VARCHAR(250)	NOT NULL
);

CREATE TABLE Conference (
	ConferenceId		VARCHAR(36)		NOT NULL,
	ConferenceName	VARCHAR(200)	NOT NULL,
	ConferenceLink	VARCHAR(250)	NOT NULL
);

CREATE TABLE Game (
	GameId					VARCHAR(36)		NOT NULL,
	GameLink				VARCHAR(250)	NOT NULL,
	HomeTeamId			VARCHAR(36)		NOT NULL,
	HomeTeamScore		INTEGER				NOT NULL,
	AwayTeamId			VARCHAR(36)		NOT NULL,
	AwayTeamScore		INTEGER				NOT NULL
);

CREATE TABLE TeamBoxScore (
	GameId						VARCHAR(36)		NOT NULL,
	TeamId						VARCHAR(36)		NOT NULL,
	TotalYards				INTEGER				NOT NULL,
	TotalPlays				INTEGER				NOT NULL,
	YardsPerPlay			DECIMAL				NOT NULL,
	FirstDowns				INTEGER				NOT NULL,
	FirstDownsPass		INTEGER				NOT NULL,
	FirstDownsRush		INTEGER				NOT NULL,
	FirstDownsPenalty	INTEGER				NOT NULL,
	Penalties					INTEGER				NOT NULL,
	PenaltyYards			INTEGER				NOT NULL
);

CREATE TABLE PassingBoxScore (
	GameId												VARCHAR(36)		NOT NULL,
	PlayerId											VARCHAR(36)		NOT NULL,
	TeamId												VARCHAR(36)		NOT NULL,
	PassCompletions								INTEGER				NOT NULL,
	PassAttempts									INTEGER				NOT NULL,
	PassCompletionPercentage			DECIMAL				NOT NULL,
	PassYards											INTEGER				NOT NULL,
	PassYardsPerAttempt						DECIMAL				NOT NULL,
	PassAdjustedYardsPerAttempt		DECIMAL				NOT NULL,
	PassTouchdowns								INTEGER				NOT NULL,
	PassInterceptions							INTEGER				NOT NULL,
	PassEfficiencyRating					DECIMAL				NOT NULL
);

CREATE TABLE RushReceiveBoxScore (
	GameId										VARCHAR(36)		NOT NULL,
	PlayerId									VARCHAR(36)		NOT NULL,
	TeamId										VARCHAR(36)		NOT NULL,
	RushAttempts							INTEGER				NULL,
	RushYards									INTEGER				NULL,
	RushYardsPerAttempt				DECIMAL				NULL,
	RushTouchdowns						INTEGER				NULL,
	Receptions								INTEGER				NULL,
	ReceiveYards							INTEGER				NULL,
	ReceiveYardsPerReception	DECIMAL				NULL,
	ReceiveTouchdowns					INTEGER				NULL
);

CREATE TABLE DefenseBoxScore (
	GameId																	VARCHAR(36)		NOT NULL,
	PlayerId																VARCHAR(36)		NOT NULL,
	TeamId																	VARCHAR(36)		NOT NULL,
	SoloTackles															INTEGER			NOT NULL,
	AssistedTackles													INTEGER			NOT NULL,
	TotalTackles														INTEGER			NOT NULL,
	TacklesForLoss													DECIMAL			NOT NULL,
	Sacks																		DECIMAL			NOT NULL,
	Interceptions														INTEGER			NULL,
	InterceptionReturnYards									INTEGER			NULL,
	InterceptionReturnYardsPerInterception	DECIMAL			NULL,
	InterceptionReturnTouchdowns						INTEGER			NULL,
	PassesDefended													INTEGER			NULL,
	FumblesRecovered												INTEGER			NULL,
	FumbleRecoveryYards											INTEGER			NULL,
	FumbleRecoveryTouchdowns								INTEGER			NULL,
	FumblesForced														INTEGER			NULL
);

CREATE TABLE KickPuntReturnBoxScore (
	GameId												VARCHAR(36)		NOT NULL,
	PlayerId											VARCHAR(36)		NOT NULL,
	TeamId												VARCHAR(36)		NOT NULL,
	KickoffReturns								INTEGER			NULL,
	KickoffReturnYards						INTEGER			NULL,
	KickoffReturnYardsPerReturn		DECIMAL			NULL,
	KickoffReturnTouchdowns				INTEGER			NULL,
	PuntReturns										INTEGER			NULL,
	PuntReturnYards								INTEGER			NULL,
	PuntReturnYardsPerReturn			DECIMAL			NULL,
	PuntReturnTouchdowns					INTEGER			NULL
);

CREATE TABLE KickPuntBoxScore (
	GameId									VARCHAR(36)		NOT NULL,
	PlayerId								VARCHAR(36)		NOT NULL,
	TeamId									VARCHAR(36)		NOT NULL,
	ExtraPointsMade					INTEGER			NULL,
	ExtraPointsAttempted		INTEGER			NULL,
	ExtraPointPercentage		DECIMAL			NULL,
	FieldGoalsMade					INTEGER			NULL,
	FieldGoalsAttempted			INTEGER			NULL,
	FieldGoalPercentage			DECIMAL			NULL,
	KickingPoints						INTEGER			NULL,
	Punts										INTEGER			NULL,
	PuntYards								INTEGER			NULL,
	PuntYardsPerAttempt			DECIMAL			NULL
);
