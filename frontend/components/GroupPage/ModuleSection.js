import React from 'react';
import LessonSection from './LessonSection';


const ModuleSection = props => (
  <div className='col-md-12'>
    {props.modules.map(module => (
      <div key={module.id}>
        <h3>Модуль: {module.name}</h3>
        <hr/>
        <LessonSection lessons={module.lessons} />
      </div>
    ))}
  </div>
);

export default ModuleSection;
