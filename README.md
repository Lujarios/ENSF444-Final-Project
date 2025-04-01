<style>
	.title {
		text-align: center;
		font-size: 70px;
		font-weight: bold;
	}
	.subtitle {
		text-align: center;
		font-style: italic;
		font-size: 30px;
	}
	.authors {
		text-align: center;
		font-size: 20px;
		padding: 10px;
	}
	.introduction {
		font-family: Arial, sans-serif;
		font-size: 18px;
		line-height: 1.6;
		text-align: justify;
		margin: 20px;
		padding: 15px;
		background-color:rgb(37, 37, 37);
		border-left: 5px solid #4CAF50;
		color: rgb(222, 222, 222);
		max-width: 90%;
	}
</style>

<hr/>
<div class="title">ENSF 444 Final Project</div>
<div class="subtitle">[ Magic: The Gathering ] Card Color Classification</div>
<div class="authors">Luca Rios & Cody Casselman</div>
<hr/>

<div class="introduction">
	<h2>Introduction</h2>
	<p>
		Magic: The Gathering (MTG) is a trading card game with around 27,000 unique cards. Each card has (at least one) color associated with it, which is a key part of the game. The colors are divided into five categories: White, Blue, Black, Red, and Green. Each color has its own unique playstyle and mechanics; however, for this project, we will be focusing on the color classification of cards.
	</p>
	<p>
		The objective of this project is to predict the color classification of MTG cards based on their oracle text (the descriptive text on the card) using a machine learning model. We will utilize a dataset containing all unique MTG cards, including their oracle text and corresponding color, to train and evaluate our model.
	</p>
	<br/>
</div>
