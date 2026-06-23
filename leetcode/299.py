class Solution:
	def get(self,ob,find):
		if find not in ob:
			return 0
		return ob[find]

	def getHint(self, secret: str, guess: str) -> str:
		result=[0,0]
		standard={}
		how_many={}
		for rs in range(len(secret)):
			if secret[rs]==guess[rs]:
				result[0]+=1
			else:
				if secret[rs] in standard:
					standard[secret[rs]]+=1
				else:
					standard[secret[rs]]=1

				if guess[rs] in how_many:
					how_many[guess[rs]]+=1
				else:
					how_many[guess[rs]]=1

		for rs in sorted(how_many.keys()):
			result[1]+=min(self.get(how_many,rs),self.get(standard,rs))

		return f"{result[0]}A{result[1]}B"