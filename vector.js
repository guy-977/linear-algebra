// const user_input = require('readline').createInterface({
// 			input: process.stdin,
// 			output: process.stdout
// 		});
class Vector {
	constructor(vector) {
		this.vector = vector;
		
	}


	magnitude(){
		let coordinates_squared = []
		let n = this.vector.length
		for(let i = 0; i < n; i++){
			coordinates_squared.push(Math.pow(this.vector[i], 2))
		}
		const sum_of_squared_coordinates = coordinates_squared.reduce((a,b) => a+b, 0)
		return Math.sqrt(sum_of_squared_coordinates)
	}

	normalize(){
		try {
			let magnitude = this.magnitude()
			return this.multiply_scalar(1/magnitude)
		} catch (RangeError){
			throw ('Cannot normalize the zero vector')
		}
	}

	plus(v){
		this.v = v.vector
		let new_coordinates = []
		let n = this.vector.length
		for(let i = 0; i < n; i++){
			new_coordinates.push(this.v[i] + this.vector[i])

		}
		return new_coordinates
	}

	minus(v){
		this.v = v.vector
		let new_coordinates = []
		let n = this.vector.length
		for(let i = 0; i < n; i++){
			new_coordinates.push(this.v[i] - this.vector[i])

		}
		return new_coordinates
	}

	multiply_scalar(s){
		let new_coordinates = []
		let n = this.vector.length
		for(let i = 0; i < n; i++){
			new_coordinates.push(s * this.vector[i])
		}
		return new_coordinates
	}

	static getVector(x1, y1, x2, y2){
		let vector = [x2-x1, y2-y1]
		return vector
	}
