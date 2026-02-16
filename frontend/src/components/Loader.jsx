import React from 'react';
import './Loader.css';

const Loader = ({ message = "Loading...", fullScreen = false }) => {
    const content = (
        <div className={`loader-container ${fullScreen ? 'fullscreen' : ''}`}>
            <div className="loader-spinner">
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
                <div className="spinner-pulse"></div>
            </div>
            {message && (
                <div className="loader-message">
                    <p className="loader-text">{message}</p>
                    <div className="loader-dots">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            )}
        </div>
    );

    if (fullScreen) {
        return (
            <div className="loader-overlay">
                {content}
            </div>
        );
    }

    return content;
};

export default Loader;
