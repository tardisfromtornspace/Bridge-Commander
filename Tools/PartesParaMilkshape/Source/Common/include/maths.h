// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  The ass engine  - (c) Graham and Hannosset           |
// |                                                       |
// |  Filename: maths.h                                    |
// |  Purpose:  matrix and vector maths                    |
// =========================================================

#ifndef __ASS_MATHS_H__ 
#define __ASS_MATHS_H__

class ass_vector;
class ass_orientation;
class ass_matrix;

class ass_vector
{
public:
	union
	{
		struct
		{
		   float x,y,z;
		};
		struct
		{
			float v[3];
		};
	};

	ass_vector( const float ax = 0.0 , const float ay = 0.0 , const float az = 0.0 )
		: x( ax ) , y( ay ) , z( az )
	{}

   void normalize(void);
   void make_empty(void);
   void set(ass_vector * src);
   void set(float _x,float _y,float _z);
   void set(float src[3]);
   float get_length(void);
   void get_vector_along_vector(ass_vector * dest, float length);
   void add(ass_vector * other);
   void scale(float scale);
   void subtract(ass_vector * other);
   void subtract_from(ass_vector * other);
   void negate(void);
   ass_vector * calculate_negate(void);
   float get_angle_xz_plane(void);
   float get_angle_yz_plane(void);
   float get_angle_xy_plane(void);

   inline ass_vector &operator-=( const ass_vector &v )
   {
	   x -= v.x;
	   y -= v.y;
	   z -= v.z;
	   return *this;
   }
   inline ass_vector &operator+=( const ass_vector &v )
   {
	   x += v.x;
	   y += v.y;
	   z += v.z;
	   return *this;
   }
};

class ass_matrix
{
public:
	union
	{
		struct
		{
			float m[4][4]; // Stored in column-major order, like OpenGL
		};
		struct
		{
			float right[4];
			float up[4];
			float front[4];
			float pos[4];
		};
		struct
		{
			float right_x;
			float right_y;
			float right_z;
			float right_w;
			float up_x;
			float up_y;
			float up_z;
			float up_w;
			float front_x;
			float front_y;
			float front_z;
			float front_w;
			float pos_x;
			float pos_y;
			float pos_z;
			float pos_w;
		};
	};
	/*

  X-Axis Y-axis Z-axis Position

  [0][0] [1][0] [2][0] [3][0]


  [0][1] [1][1] [2][1] [3][1]


  [0][2] [1][2] [2][2] [3][2]


  -------LEFT OVERS----------
  [0][3] [1][3] [2][3] [3][3]

	*/

	ass_matrix()
	{
		reset();
	}

	void reset(void);
	ass_matrix * multiply_by(ass_matrix * s);
	ass_matrix * calculate_inverse(void);
	ass_matrix * find_transpose(void);
	void from_euler(float rx, float ry, float rz);
	void from_vectors(ass_vector *a, ass_vector *b, ass_vector *c, ass_vector *t);
	void make_vector_rotate(ass_vector *v, float amount);
	void to_euler(float *rx, float *ry, float *rz);
	void to_vectors(ass_vector *a, ass_vector *b, ass_vector *c);
	#ifdef D3D_SUPPORT
		D3DMATRIX temp_d3d;
		D3DMATRIX * to_d3d(void);
	#endif
	void apply_to_vector(ass_vector * v);
	void apply_to_vector(float *x, float *y, float *z);
	void apply_to_vector(float *v[3]);
	void rotate(float rx, float ry, float rz);
	void rotate_x(float rx);
	void rotate_y(float ry);
	void rotate_z(float rz);
	void translate(ass_vector *t);
	void translate(float x, float y, float z);
	void scale(float s);
   void scale(float x,float y,float z);
	void flip_z(void);
};

class ass_orientation
{
public:
	ass_vector right,up,front;
	ass_matrix temp_matrix;

	ass_orientation()
	{
		reset();
	}

   void turn_z(float amount);
   void turn_y_cheat(float amount);
   void turn_y(float amount);
   void turn_x(float amount);
   void from_vectors(ass_vector * _right, ass_vector * _up, ass_vector * _front);
   void from_vector(ass_vector * _front);
   ass_matrix * to_matrix(void);
   void reset(void);
};

#endif



















