import React from 'react';
import { VerticalTimeline, VerticalTimelineElement } from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';

function Timeline({ achievements }) {
  // Map the achievements to timeline elements
  const timelineElements = achievements.map((achievement) => (
    <VerticalTimelineElement
      key={achievement[0]}
      date={new Date(achievement[1].date).toLocaleDateString()}
      icon={<i className="fas fa-trophy"></i>}
    >
      <h3>{achievement[1].title}</h3>
      <h5>{achievement[1].patch}</h5>
      <p>{achievement[1].description}</p>
    </VerticalTimelineElement>
  ));

  return (
    <VerticalTimeline>
      {timelineElements}
    </VerticalTimeline>
  );
}

export default Timeline;
