var TennisGame2 = function(player1Name, player2Name) {
    this.P1point = 0;
    this.P2point = 0;

    this.P1res = "";
    this.P2res = "";

    this.player1Name = player1Name;
    this.player2Name = player2Name;
};

TennisGame2.prototype.getScore = function() {
    let score = "";

    score = this.handleDraws(score);

    score = this.handleEndGameScores(score);

    score = this.handleNormalScoring(score);

    return score;
};

TennisGame2.prototype.handleDraws = function(score) {
    if (this.P1point === this.P2point) {
        if (this.P1point > 2) {
            score = "Deuce";
        } else {
            score = this.convertNumericScoresToWords(this.P1point);
            score += "-All";
        }
    }
    return score;
}

TennisGame2.prototype.handleEndGameScores = function(score) {
    if ((this.P1point > 3 || this.P2point > 3) && !score) {
        const difference = this.P1point - this.P2point;
        const abs_difference = difference < 0 ? -difference : difference;
        if (abs_difference === 1) {
            score = this.handleAdvantages(difference);
        } else {
            score = this.handleWins(difference)
        }
    }
    return score;
}

TennisGame2.prototype.handleAdvantages = function(difference) {
    if (difference > 0) {
        score = "Advantage player1"
    } else {
        score = "Advantage player2"
    }
    return score;
}

TennisGame2.prototype.handleWins = function(difference) {
    if (difference > 0) {
        score = "Win for player1"
    } else {
        score = "Win for player2"
    }
    return score;
}

TennisGame2.prototype.handleNormalScoring = function(score) {
    if (!score) {
        this.P1res = this.convertNumericScoresToWords(this.P1point);
        this.P2res = this.convertNumericScoresToWords(this.P2point);
        score = this.P1res + "-" + this.P2res;
    }
    return score;
}

TennisGame2.prototype.convertNumericScoresToWords = function(numericalScore) {
    let wordScore = "";
    switch (numericalScore) {
        case 0:
            wordScore = "Love";
            break;
        case 1:
            wordScore = "Fifteen";
            break;
        case 2:
            wordScore = "Thirty";
            break;
        case 3:
            wordScore = "Forty";
            break;
    }
    return wordScore;
}

TennisGame2.prototype.wonPoint = function(player) {
    if (player === this.player1Name)
        this.P1point++;
    else
        this.P2point++;
};

if (typeof window === "undefined") {
    module.exports = TennisGame2;
}