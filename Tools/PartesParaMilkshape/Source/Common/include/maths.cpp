// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  The ass engine  - (c) Graham and Hannosset           |
// |                                                       |
// |  Filename: maths.cpp                                  |
// |  Purpose:  Mostly Matrix and vector manipulation code |
// =========================================================

#include "maths.h"
#include <math.h>

void ass_vector::normalize(void)
{
	float length=get_length();
	x=x/length;
	y=y/length;
	z=z/length;
}

void ass_vector::make_empty(void)
{
   x=y=z=0;
}

void ass_vector::set(ass_vector * src)
{
   x=src->x;
   y=src->y;
   z=src->z;
}

void ass_vector::set(float _x,float _y,float _z)
{
   x=_x;
   y=_y;
   z=_z;
}

void ass_vector::set(float src[3])
{
   x=src[0];
   y=src[1];
   z=src[2];
}

float ass_vector::get_length(void)
{
	float length=(float)sqrt(x*x+y*y+z*z);
	if (length==0) length=1;
	return length;
}

void ass_vector::get_vector_along_vector(ass_vector * dest, float length)
{
   float len=get_length();

   dest->x=x*length/len;
   dest->y=y*length/len;
   dest->z=z*length/len;
}

void ass_vector::add(ass_vector * other)
{
   x+=other->x;
   y+=other->y;
   z+=other->z;
}

void ass_vector::scale(float scale)
{
   x*=scale;
   y*=scale;
   z*=scale;
}

void ass_vector::subtract(ass_vector * other)
{
   x-=other->x;
   y-=other->y;
   z-=other->z;
}

void ass_vector::subtract_from(ass_vector * other)
{
   x=other->x-x;
   y=other->y-y;
   z=other->z-z;
}

void ass_vector::negate(void)
{
   x=-x;
   y=-y;
   z=-z;
}

ass_vector temp_negate;
ass_vector * ass_vector::calculate_negate(void)
{
   temp_negate.set(this);
   temp_negate.negate();
   return &temp_negate;
}

#define PI (float)3.14159

float ass_sin(float angle)
{
	double new_angle=angle*PI/180;
	float answer=sin(new_angle);
	return answer;
}

float ass_cos(float angle)
{
	double new_angle=angle*PI/180;
	float answer=cos(new_angle);
	return answer;
}

float ass_tan(float angle)
{
	double new_angle=angle*PI/180;
	float answer=tan(new_angle);
	return answer;
}

float ass_arc_sin(float input)
{
	float answer=asin(input);
	double newans=answer*180/PI;
	if (newans<-180) newans+=360;
	if (newans>180) newans-=360;
	return newans;
}

float ass_arc_cos(float input)
{
	float answer=acos(input);
	double newans=answer*180/PI;
	if (newans<-180) newans+=360;
	if (newans>180) newans-=360;
	return newans;
}

float ass_arc_tan(float input)
{
	float answer=atan(input);
	double newans=answer*180/PI;
	if (newans<-90) newans+=180;
	if (newans>90) newans-=180;
	return newans;
}

float wise_arc_tan(float a, float b)
{
   // Avoid the bad div/0 case
   if (b==0)
   {
      if (a<0) return -90; else return 90;
   }

   float angle=ass_arc_tan(a/b);

   if (angle>180) angle-=360;

   if ((a>=0) && (b>=0)) return angle;
   if ((a<0) && (b<0)) return angle-180;
   if (a<0) return angle;
   if (b<0) return angle-180;

   return 0; // should never happen
}

float ass_vector::get_angle_xz_plane(void)
{
   return wise_arc_tan(x,z);
}

float ass_vector::get_angle_yz_plane(void)
{
   return wise_arc_tan(y,z);
}

float ass_vector::get_angle_xy_plane(void)
{
   return wise_arc_tan( x , y );
}

void ass_matrix::reset(void) // Sets to identity matrix
{
	int i,j;
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			if (i==j) m[i][j]=1; else m[i][j]=0;
		}
	}
}

ass_matrix * ass_matrix::multiply_by(ass_matrix * s)
{
	float nm[4][4];
	int i,j;
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			nm[i][j]=0;
			int k;
			for (k=0;k<4;k++)
			{
				nm[i][j]+=m[i][k]*s->m[k][j];
			}
		}
	}
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			m[i][j]=nm[i][j];
		}
	}

	return this;
}

ass_matrix temp_inverse;
ass_matrix * ass_matrix::calculate_inverse(void)
{
	// (Not my code)

	float Tx, Ty, Tz;

	// The rotational part of the matrix is simply the transpose of the
	// original matrix.
	temp_inverse.m[0][0] = m[0][0];
	temp_inverse.m[1][0] = m[0][1];
	temp_inverse.m[2][0] = m[0][2];

	temp_inverse.m[0][1] = m[1][0];
	temp_inverse.m[1][1] = m[1][1];
	temp_inverse.m[2][1] = m[1][2];

	temp_inverse.m[0][2] = m[2][0];
	temp_inverse.m[1][2] = m[2][1];
	temp_inverse.m[2][2] = m[2][2];

	// The right column vector of the matrix should always be [ 0 0 0 1 ]
	// In most cases. . . you don't need this column at all because it'll 
	// never be used in the program, but since this code is used with GL
	// and it does consider this column, it is here.
	temp_inverse.m[0][3] = temp_inverse.m[1][3] = temp_inverse.m[2][3] = 0;
	temp_inverse.m[3][3] = 1;

	// The translation components of the original matrix.
	Tx = m[3][0];
	Ty = m[3][1];
	Tz = m[3][2];

	// Rresult = -(Tm * Rm) to get the translation part of the inverse
	temp_inverse.m[3][0] = -( m[0][0] * Tx + m[0][1] * Ty + m[0][2] * Tz );
	temp_inverse.m[3][1] = -( m[1][0] * Tx + m[1][1] * Ty + m[1][2] * Tz );
	temp_inverse.m[3][2] = -( m[2][0] * Tx + m[2][1] * Ty + m[2][2] * Tz );


	return &temp_inverse;
}

ass_matrix temp_transpose;
ass_matrix * ass_matrix::find_transpose(void)
{
	int i,j;
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			if (i==j) continue;

			temp_transpose.m[i][j]=m[j][i];
			temp_transpose.m[j][i]=m[i][j];
		}
	}

	return &temp_transpose;
}

void ass_matrix::from_euler(float rx, float ry, float rz)
{
	reset();

	rotate(rx,ry,rz);
}

void ass_matrix::from_vectors(ass_vector *a, ass_vector *b, ass_vector *c, ass_vector *t)
{
	reset();

	m[0][0]=a->x;
	m[0][1]=a->y;
	m[0][2]=a->z;
	m[1][0]=b->x;
	m[1][1]=b->y;
	m[1][2]=b->z;
	m[2][0]=c->x;
	m[2][1]=c->y;
	m[2][2]=c->z;
	if (t)
	{
		m[3][0]=t->x;
		m[3][1]=t->y;
		m[3][2]=t->z;
	} else
	{
		m[3][0]=0;
		m[3][1]=0;
		m[3][2]=0;
	}
}

void ass_matrix::to_euler(float *rx, float *ry, float *rz) // Very rough indeed!
{
	float x_1=-ass_arc_sin(m[1][2]);
	float x_2=+ass_arc_sin(m[2][1]);
	*rx=(x_1+x_2)/2;

	float y_1=-ass_arc_sin(m[0][2]);
	float y_2=+ass_arc_sin(m[2][0]);
	*ry=(y_1+y_2)/2;

	float z_1=-ass_arc_sin(m[0][1]);
	float z_2=+ass_arc_sin(m[1][0]);
	*rz=(z_1+z_2)/2;
}

void ass_matrix::to_vectors(ass_vector *a, ass_vector *b, ass_vector *c)
{
   if (a)
   {
	   a->x=m[0][0];
	   a->y=m[0][1];
	   a->z=m[0][2];
   }
   if (b)
   {
	   b->x=m[1][0];
	   b->y=m[1][1];
	   b->z=m[1][2];
   }
   if (c)
   {
	   c->x=m[2][0];
	   c->y=m[2][1];
	   c->z=m[2][2];
   }
}

#ifdef D3D_SUPPORT
	D3DMATRIX * ass_matrix::to_d3d(void)
	{
		ass_matrix * temp=find_transpose();

		temp_d3d._11=temp->m[1][1];
		temp_d3d._12=temp->m[1][2];
		temp_d3d._13=temp->m[1][3];
		temp_d3d._14=temp->m[1][4];
		temp_d3d._21=temp->m[2][1];
		temp_d3d._22=temp->m[2][2];
		temp_d3d._23=temp->m[2][3];
		temp_d3d._24=temp->m[2][4];
		temp_d3d._31=temp->m[3][1];
		temp_d3d._32=temp->m[3][2];
		temp_d3d._33=temp->m[3][3];
		temp_d3d._34=temp->m[3][4];
		temp_d3d._41=temp->m[4][1];
		temp_d3d._42=temp->m[4][2];
		temp_d3d._43=temp->m[4][3];
		temp_d3d._44=temp->m[4][4];
		return &temp_d3d;
	}
#endif

void ass_matrix::apply_to_vector(ass_vector * v)
{
	float *_v[3];
	_v[0]=&v->x;
	_v[1]=&v->y;
	_v[2]=&v->z;
	apply_to_vector(_v);
}

void ass_matrix::apply_to_vector(float *x, float *y, float *z)
{
	float *_v[3];
	_v[0]=x;
	_v[1]=y;
	_v[2]=z;
	apply_to_vector(_v);
}

void ass_matrix::apply_to_vector(float *v[3])
{
	float final[4];
	float s[4];
	s[0]=*v[0];
	s[1]=*v[1];
	s[2]=*v[2];
	s[3]=1;

	int i;
	for (i=0;i<4;i++)
	{
		final[i]=0;
		int k;
		for (k=0;k<4;k++)
		{
			final[i]+=m[k][i]*s[k];
		}
	}
	for (i=0;i<3;i++)
	{
		*v[i]=final[i];
	}
}

void ass_matrix::rotate(float rx, float ry, float rz)
{
	if (rx!=0) rotate_x(rx);
	if (ry!=0) rotate_y(ry);
	if (rz!=0) rotate_z(rz);
}

void ass_matrix::rotate_x(float rx)
{
	ass_matrix rotater;

	rotater.m[1][1]=ass_cos(rx);
	rotater.m[1][2]=-ass_sin(rx);
	rotater.m[2][1]=ass_sin(rx);
	rotater.m[2][2]=ass_cos(rx);

	multiply_by(&rotater);
}

void ass_matrix::rotate_y(float ry)
{
	ass_matrix rotater;

	rotater.m[0][0]=ass_cos(ry);
	rotater.m[0][2]=-ass_sin(ry);
	rotater.m[2][0]=ass_sin(ry);
	rotater.m[2][2]=ass_cos(ry);

	multiply_by(&rotater);
}

void ass_matrix::rotate_z(float rz)
{
	ass_matrix rotater;

	rotater.m[0][0]=ass_cos(rz);
	rotater.m[0][1]=-ass_sin(rz);
	rotater.m[1][0]=ass_sin(rz);
	rotater.m[1][1]=ass_cos(rz);

	multiply_by(&rotater);
}

void ass_matrix::translate(ass_vector *t)
{
	translate(t->x,t->y,t->z);
}

void ass_matrix::translate(float x, float y, float z)
{
	m[3][0]+=x;
	m[3][1]+=y;
	m[3][2]+=z;
}

void ass_matrix::scale(float s)
{
	m[0][0]*=s;
	m[1][1]*=s;
	m[2][2]*=s;
}

void ass_matrix::scale(float x,float y,float z)
{
	m[0][0]*=x;
	m[1][1]*=y;
	m[2][2]*=z;
}

void ass_matrix::flip_z(void)
{
	m[0][2]*=-1;
	m[1][2]*=-1;
	m[2][2]*=-1;
	m[3][2]*=-1;
}

void ass_matrix::make_vector_rotate(ass_vector *v, float amount)
{
	reset();

   float c = ass_cos(amount);
   float s = ass_sin(amount);
   float cc = 1 - c;

   m[0][0] = (cc * v->x * v->x) + c;
   m[0][1] = (cc * v->x * v->y) + (v->z * s);
   m[0][2] = (cc * v->x * v->z) - (v->y * s);

   m[1][0] = (cc * v->x * v->y) - (v->z * s);
   m[1][1] = (cc * v->y * v->y) + c;
   m[1][2] = (cc * v->z * v->y) + (v->x * s);

   m[2][0] = (cc * v->x * v->z) + (v->y * s);
   m[2][1] = (cc * v->y * v->z) - (v->x * s);
   m[2][2] = (cc * v->z * v->z) + c;
}

void ass_orientation::reset(void)
{
	right.y=right.z=up.x=up.z=front.x=front.y=0;
	right.x=up.y=front.z=1;
}

ass_matrix * ass_orientation::to_matrix(void)
{
	temp_matrix.from_vectors(&right,&up,&front,0);
	return &temp_matrix;
}

// Only two need specifying
void ass_orientation::from_vectors(ass_vector * _right, ass_vector * _up, ass_vector * _front)
{
   if (_right)
   {
      right.x=_right->x;
      right.y=_right->y;
      right.z=_right->z;
   }
   if (_up)
   {
      up.x=_up->x;
      up.y=_up->y;
      up.z=_up->z;
   }
   if (_front)
   {
      front.x=_front->x;
      front.y=_front->y;
      front.z=_front->z;
   }
   right.normalize();
   up.normalize();
   front.normalize();
}

void ass_orientation::turn_x(float amount)
{
	ass_matrix mymatrix;
	mymatrix.make_vector_rotate(&right,amount);
	to_matrix()->multiply_by(&mymatrix)->to_vectors(&right,&up,&front);
}

void ass_orientation::turn_y(float amount)
{
	ass_matrix mymatrix;
	mymatrix.make_vector_rotate(&up,amount);
	to_matrix()->multiply_by(&mymatrix)->to_vectors(&right,&up,&front);
}

void ass_orientation::turn_y_cheat(float amount)
{
	ass_matrix mymatrix;
   ass_vector temp;
   temp.x=temp.z=0;
   temp.y=1;
	mymatrix.make_vector_rotate(&temp,amount);
	to_matrix()->multiply_by(&mymatrix)->to_vectors(&right,&up,&front);
}

void ass_orientation::turn_z(float amount)
{
	ass_matrix mymatrix;
	mymatrix.make_vector_rotate(&front,amount);
	to_matrix()->multiply_by(&mymatrix)->to_vectors(&right,&up,&front);
}

