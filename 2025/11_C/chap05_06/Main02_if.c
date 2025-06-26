#include <stdio.h>
int main02() {
	char grade;
	int score;
	printf("점수를 입력하세요\n");
	scanf("%d", &score);
	if (score >= 90 && score <= 100)
		grade = 'A';
	if (score >= 80 && score < 90)
		grade = 'B';
	if (score >= 70 && score < 80)
		grade = 'C';
	if (score >= 60 && score < 70)
		grade = 'D';
	if (score < 60)
		grade = 'F';
	printf("score = %d, grade = %c\n", score, grade);
    return 0;
}

