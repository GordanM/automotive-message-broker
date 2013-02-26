#ifndef _FAKEIDLHEADER_H_
#define _FAKEIDLHEADER_H_

/** @module Vehicle **/

/** @moduleComment
*
* Details.
*
* \def-api-feature http://tizen.org/api/vehicle
* \brief Allows access to the vehicle API
*
**/

/** @interface VehicleObject */
/**
* @attributeName  vehicle
* @type Vehicle
* @access 
**/

/** @raw Tizen implements VehicleObject; **/

/** @interface VehiclePropertyType **/
/** @attributeName value
 *  @type object
 *  @access readonly
 *
 *  @attributeName timeStamp
 *  @type Date
 *  @access readonly
**/

/** @interface Vehicle **/
/** @method sequence<DOMString> getSupported();
 *  @method VehiclePropertyType get(DOMString event);
 *  @method void set(DOMString event, object value);
 *  @method sequence<VehiclePropertyTypes> getHistory(DOMString type, Date startTime, Date endTime);
 **/


#endif
