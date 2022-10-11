var TennisGame1 = function(player1Name, player2Name) {
    this.m_score1 = 0;
    this.m_score2 = 0;
    this.player1Name = player1Name;
    this.player2Name = player2Name;
};

TennisGame1.prototype.wonPoint = function(playerName) {
    if (playerName === this.player1Name)
        this.m_score1 += 1;
    else
        this.m_score2 += 1;
};

TennisGame1.prototype.getScore = function() {
    let score = "";
    
    score = this.checkEqualScore(score);

    score = this.checkHighScores(score);
    
    score = this.handleRestOfScores(score);

    return score;
};

TennisGame1.prototype.checkEqualScore = function(score) {
    if (this.m_score1 === this.m_score2) {
        if (this.m_score1 >= 3) {
            score = "Deuce"
        } else {
            score = this.convertNumericalScore(this.m_score1, score);
            score += "-";
            score += "All"
        }
    }
    return score
}

TennisGame1.prototype.checkHighScores = function(score) {
    if ((this.m_score1 >= 4 || this.m_score2 >= 4) && !score) {

        const minusResult = this.m_score1 - this.m_score2;

        score = this.checkAdvantage(minusResult, score);

        score = this.checkWin(minusResult, score);
    }
    return score
}

TennisGame1.prototype.checkAdvantage = function(minusResult, score) {
    if (minusResult === 1) {
        score = "Advantage player1"
    } else if (minusResult === -1) {
        score = "Advantage player2"
    }
    return score;
}

TennisGame1.prototype.checkWin = function(minusResult, score) {
    if (minusResult >= 2) {
        score = "Win for player1";
    } else if (minusResult <= -2) {
        score = "Win for player2";
    }
    return score;
}

TennisGame1.prototype.handleRestOfScores = function(score) {
    if (!score) {
        score = this.convertNumericalScore(this.m_score1, score);
        score += "-";
        score = this.convertNumericalScore(this.m_score2, score)
    }
    return score;
}

TennisGame1.prototype.convertNumericalScore = function(numericalScore, wordScore) {
    switch (numericalScore) {
        case 0:
            wordScore += "Love";
            break;
        case 1:
            wordScore += "Fifteen";
            break;
        case 2:
            wordScore += "Thirty";
            break;
        case 3:
            wordScore += "Forty";
            break;
    }
    return wordScore;
}

if (typeof window === "undefined") {
    module.exports = TennisGame1;
}
