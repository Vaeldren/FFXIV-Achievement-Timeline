import React from 'react';
import { VerticalTimeline, VerticalTimelineElement } from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';

function Timeline({ achievements }) {
  // Map the achievements to timeline elements
  const timelineElements = achievements.map((achievement) => (
    <VerticalTimelineElement
      key={achievement.id}
      date={new Date(achievement.date).toLocaleDateString()}
      icon={<i className="fas fa-trophy"></i>}
    >
      <h3>{achievement.title}</h3>
      <p>{achievement.description}</p>
    </VerticalTimelineElement>
  ));

  return (
    <VerticalTimeline>
      {timelineElements}
    </VerticalTimeline>
  );
}

export default Timeline;
