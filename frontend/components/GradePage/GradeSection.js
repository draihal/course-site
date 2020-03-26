import React from 'react';
import AddGrade from './AddGrade';
import UpdateGrade from './UpdateGrade';

const GradeSection = props => (
  <div>
    {(!props.homework.grade && (
      <AddGrade homework={props.homework} teacherId={props.teacherId} token={props.token}/>
    )) || <UpdateGrade homework={props.homework} teacherId={props.teacherId} token={props.token} grade={props.homework.grade}/>}
  </div>
);

export default GradeSection;
